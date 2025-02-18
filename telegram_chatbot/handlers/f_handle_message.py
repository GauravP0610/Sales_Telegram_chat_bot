import logging as logger
import time
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, Contact
from telegram.ext import ContextTypes
from f_llm_functions import generate_gemini_response
from f_mongo_functions import get_conversation, get_user_details, save_message, save_user_details, save_user_faq, get_message
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.f_prompts import generate_user_message_prompt
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.handlers.f_request_contact import request_contact
from telegram_chatbot.handlers.f_start_command import start_command
from telegram_chatbot.t_reply_markup_keyboards import reply_markup_main

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    chat_id = update.effective_chat.id
    user_message = update.message.text    
    user_details = get_user_details(chat_id)

    # If we are awaiting a phone number, redirect message to request_contact
    if context.chat_data.get("awaiting_contact") or context.chat_data.get("awaiting_confirmation"):
        await request_contact(update, context)
        return  # Stop further execution in handle_message

    save_user_faq(chat_id, user_message)

    if not user_details:
        save_message(chat_id, sender="user", message=user_message)  
        sticker_file_id = "CAACAgUAAxkBAAMPZ5aVDJi5Wnf5CNUXNsR3Uxgitt8AAhcTAAIFWLhUUE7KGQOin_k2BA" 
        await context.bot.send_sticker(chat_id=chat_id, sticker=sticker_file_id)

        message = get_message("welcome_message")
        await send_llm_response_line_by_line(message, update, context)

        user_details = {
            "first_name": user.first_name,
            "last_name": user.last_name or "N/A",
            "username": user.username or "N/A",
            "language_code": user.language_code or "N/A",
            "is_premium": getattr(user, "is_premium", False),
        }
        save_user_details(chat_id, user_details) 

        await simulate_typing(context, chat_id, 3)
        message = get_message("welcome_back_message")
        await update.message.reply_text(message)    
        save_message(chat_id, sender="bot", message=message)

        await simulate_typing(context, chat_id, 3)
        message = get_message("services_offered")
        await update.message.reply_text(message, reply_markup=reply_markup_main) 
        save_message(chat_id, sender="bot", message=message)  
        return   

    # Handle active handler logic
    if context.chat_data.get('active_handler') == 'chat_kapil_mittal':        
        past_conversation = get_conversation(chat_id, limit=20)
        existing_user_details = get_user_details(chat_id)
        save_message(chat_id, sender="user", message=user_message)
        
        prompt = await generate_user_message_prompt(existing_user_details, past_conversation, user_message)
        try:
            bot_raw_response = generate_gemini_response(prompt)
            print(bot_raw_response)
        except Exception as e:
            print("LLM error:", e)
            fallback_reply = get_message("fallback_reply")
            await update.message.reply_text(fallback_reply)
            return        

        await send_llm_response_line_by_line(bot_raw_response, update, context)
        return

    # Regular conversation flow
    past_conversation = get_conversation(chat_id, limit=20)
    existing_user_details = get_user_details(chat_id)
    save_message(chat_id, sender="user", message=user_message)
    
    prompt = await generate_user_message_prompt(existing_user_details, past_conversation, user_message)

    try:
        bot_raw_response = generate_gemini_response(prompt)
        print(bot_raw_response)
    except Exception as e:
        print("LLM error:", e)
        fallback_reply = get_message("fallback_reply")
        await update.message.reply_text(fallback_reply)
        return    

    await send_llm_response_line_by_line(bot_raw_response, update, context)

    # Handling photos and documents
    if update.message.photo:
        photo = update.message.photo[-1]  
        file_id = photo.file_id
        file = await context.bot.get_file(file_id)

        file_metadata = {
            "file_id": file_id,
            "file_type": "photo",
            "file_size": photo.file_size,
            "file_url": file.file_path
        }

        save_message(chat_id, sender="user", file=file_metadata)
        await update.message.reply_text(get_message("photo_received"))

    elif update.message.document:
        document = update.message.document
        file_id = document.file_id
        file = await context.bot.get_file(file_id)

        file_metadata = {
            "file_id": file_id,
            "file_name": document.file_name,
            "file_type": document.mime_type,
            "file_size": document.file_size,
            "file_url": file.file_path
        }

        save_message(chat_id, sender="user", file=file_metadata)
        await update.message.reply_text(get_message("file_received").replace("{file_name}", document.file_name))

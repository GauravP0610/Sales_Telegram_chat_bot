import time
from telegram import InlineKeyboardButton, Update
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.t_reply_markup_keyboards import reply_markup_main, reply_markup_kapil
from f_mongo_functions import save_message, get_user_details, save_user_details, get_message
from telegram_chatbot.handlers.f_request_contact import request_contact

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    user = update.message.from_user
    chat_id = update.effective_chat.id
    user_details = get_user_details(chat_id)
    user_first_name = user.first_name

    if not user_details:

        sticker_file_id = "CAACAgUAAxkBAAMPZ5aVDJi5Wnf5CNUXNsR3Uxgitt8AAhcTAAIFWLhUUE7KGQOin_k2BA" 
        await context.bot.send_sticker(chat_id=chat_id, sticker=sticker_file_id)

        message = get_message("welcome_message").replace("{user_first_name}", user_first_name)
            
        await send_llm_response_line_by_line(message, update, context)

        user_details = {
            "first_name": user_first_name,
            "last_name": user.last_name or "N/A",  # Handle None values
            "username": user.username or "N/A",
            "language_code": user.language_code or "N/A",
            "is_premium": getattr(user, "is_premium", False),
        }
        save_user_details(chat_id, user_details)    

        await simulate_typing(context, chat_id, 3)
        message = get_message("welcome_back_message").replace("{user_first_name}", user_first_name)
        await update.message.reply_text(message)    
        save_message(chat_id, sender="bot", message=message)
        await simulate_typing(context, chat_id, 3)
        message = get_message("services_offered")
        await update.message.reply_text(message, reply_markup=reply_markup_main) 
        save_message(chat_id, sender="bot", message=message)  

        return    
    
    sticker_file_id = "CAACAgUAAxkBAAMPZ5aVDJi5Wnf5CNUXNsR3Uxgitt8AAhcTAAIFWLhUUE7KGQOin_k2BA" 
    await context.bot.send_sticker(chat_id=chat_id, sticker=sticker_file_id)     

    time.sleep(2)
    message = get_message("welcome_back_message").replace("{user_first_name}", user_first_name)
    await update.message.reply_text(message)    
    save_message(chat_id, sender="bot", message=message)
    await simulate_typing(context, chat_id, 3)
    
    message = get_message("services_offered")
    await update.message.reply_text(message, reply_markup=reply_markup_main) 
    save_message(chat_id, sender="bot", message=message)


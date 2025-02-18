import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import  ContextTypes
from f_mongo_functions import save_message, save_user_detail, get_message
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.handlers.f_request_contact import request_contact
from telegram_chatbot.t_reply_markup_keyboards import reply_markup_breakoutai

async def breakoutai_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    
    chat_id = query.message.chat_id or update.effective_chat.id
    user_first_name = query.from_user.first_name

    await query.answer() 
    save_message(chat_id, sender="user", message="Provide me Breakoutai Details")  
    save_user_detail(chat_id, "selected_service", 'breakoutai')

    message = get_message("breakoutai_details")
    await send_llm_response_line_by_line(message, update, context)    
    
    await simulate_typing(context, chat_id, 5) 
    message = get_message("how_would_you_like_to_proceed")
    await query.message.reply_text(
        message,
        reply_markup=reply_markup_breakoutai
    )   
    save_message(chat_id, sender="bot", message=message)



import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import  ContextTypes

from f_mongo_functions import save_message
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.handlers.f_ensure_contact import ensure_contact
from telegram_chatbot.handlers.f_request_contact import request_contact
from telegram_chatbot.t_reply_markup_keyboards import reply_markup_breakoutai, reply_markup_capital



async def subscribe_breakoutai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id

    user_first_name = query.from_user.first_name
    await query.answer() 
    save_message(chat_id, sender="user", message="I want to subscribe to BreakoutAI")  

    message = f"""
        Finding the best plan for you ⏳
        {user_first_name} Ji, I need some more details to find the right plan for you ✅
    """
    await send_llm_response_line_by_line(message, update, context)    
    
    await simulate_typing(context, chat_id, 6) 
    message = f"How much Capital do you have to invest? There is NO minimum capital requirement for BreakoutAI!💰" 
    await query.message.reply_text(
        message,
        reply_markup = reply_markup_capital
    )   
    save_message(chat_id, sender="bot", message=message)        
    
  
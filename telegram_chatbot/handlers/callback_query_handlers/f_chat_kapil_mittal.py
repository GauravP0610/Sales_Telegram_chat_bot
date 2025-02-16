
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import  ContextTypes

from f_mongo_functions import save_message
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing


async def chat_kapil_mittal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() 
    chat_id = query.message.chat_id
    user_first_name = query.from_user.first_name # Acknowledge the callback query
    time.sleep(2)
    await simulate_typing(context, chat_id, 2)
    message = f"Connecting your chat with Kapil Mittal, please wait... ⏳" 
    await query.message.reply_text(
        message
    )   
    save_message(chat_id, sender="bot", message=message)  

    time.sleep(4)
    await simulate_typing(context, chat_id, 2)
    message = f"You are now connected! Please ask your questions ✅" 
    await query.message.reply_text(
        message
    )   
    save_message(chat_id, sender="bot", message=message)      


    context.chat_data['active_handler'] = 'chat_kapil_mittal'



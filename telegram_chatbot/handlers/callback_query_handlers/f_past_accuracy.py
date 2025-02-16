
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import  ContextTypes

from f_mongo_functions import save_message
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.t_reply_markup_keyboards import reply_markup_past_accuracy, reply_markup_breakoutai


async def past_accuracy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    user_first_name = query.from_user.first_name


    await query.answer() 
    save_message(chat_id, sender="user", message="What is the past accuracy?")  

    await simulate_typing(context, chat_id, 1)
    message = f"Great that you asked!" 
    await query.message.reply_text(
        message
    )   
    save_message(chat_id, sender="bot", message=message)  
    
    time.sleep(4)
    await simulate_typing(context, chat_id, 5)
    message = f"{user_first_name} Ji, I am the only analyst in the markets who share his verified PnL transparently. " 
    await query.message.reply_text(
        message
    )   
    save_message(chat_id, sender="bot", message=message)  
    
    time.sleep(5)
    await simulate_typing(context, chat_id, 5)    
    message = f"You can click on the link below to see my verified PnL from Zerodha or Fyers " 
    await query.message.reply_text(
        message
    )   
    save_message(chat_id, sender="bot", message=message)        
 
    
    time.sleep(5)
    await simulate_typing(context, chat_id, 3) 
    message = f"Here are the links 👇" 
    await query.message.reply_text(
        message,
        reply_markup=reply_markup_past_accuracy
    )   
    save_message(chat_id, sender="bot", message=message) 

    time.sleep(5)
    await simulate_typing(context, chat_id, 5) 
    message = f"Congratulations {user_first_name} Ji 🎉, you are eligible for 50% extra discount on BTST plans! 👇" 
    await query.message.reply_text(
        message,
        reply_markup=reply_markup_breakoutai
    )   
    save_message(chat_id, sender="bot", message=message)              



import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import  ContextTypes

from f_mongo_functions import save_message
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.t_reply_markup_keyboards import reply_markup_btst_strategy



async def btst_strategy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    user_first_name = query.from_user.first_name

    await query.answer() 
    save_message(chat_id, sender="user", message="Tell me about the BTST Strategy")  

    message = f"""
        {user_first_name} Ji, I have spent last 6 years to develop a highly successfull BTST strategy. 👨🏻‍💻
       
         These kind of strategies have always been hidden from small traders. 

         I have achieved 95% accuracy with this strategy! 💯
         
         My goal is to help traders in the market by letting you use these profitable strategies to make money! 😄

         I suggest only highly liquid stocks so the strategy works even when markets are falling. ✅

         I spend more than 5 hours every day anlysing charts to find the best BTST trades for you! 🚀
        
    """
    await send_llm_response_line_by_line(message, update, context)
 
    await simulate_typing(context, chat_id, 5) 
    message = f"{user_first_name} Ji, would you like to start BTST trading? 😄 " 
    await query.message.reply_text(
        message,
        reply_markup=reply_markup_btst_strategy
    )   
    save_message(chat_id, sender="bot", message=message)      
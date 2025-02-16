
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import  ContextTypes

from f_mongo_functions import save_message, save_user_detail
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.t_reply_markup_keyboards import reply_markup_btst



async def btst_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    user_first_name = query.from_user.first_name

    await query.answer() 
    save_message(chat_id, sender="user", message="Provide me BTST Details")  
    save_user_detail(chat_id, "selected_service", 'btst')

    message = f"""
         Everyday I will send you 5 BTST stocks to trade at 2:30 PM ⏱️.
         You buy these BTST stocks anytime before 3:30 PM 
         Next day we sell the stocks at the provided Target and make profits! 🚀         
         Each stock will have exact Target and SL for next day ✅
         {user_first_name} Ji, you make 3-5% in profits everyday with BTST trades.

    """
    await send_llm_response_line_by_line(message, update, context)
 
    await simulate_typing(context, chat_id, 5) 
    message = f"{user_first_name} Ji, how would you like to proceed? 😄 " 
    await query.message.reply_text(
        message,
        reply_markup=reply_markup_btst
    )   
    save_message(chat_id, sender="bot", message=message)      
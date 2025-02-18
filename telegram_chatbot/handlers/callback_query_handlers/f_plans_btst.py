import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import  ContextTypes

from f_mongo_functions import save_message, get_message
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_ask_for_capital import ask_for_capital
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.handlers.f_request_contact import request_contact
from telegram_chatbot.t_reply_markup_keyboards import reply_markup_capital



async def plans_btst(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    user_first_name = query.from_user.first_name

    await query.answer() 
    save_message(chat_id, sender="user", message="Tell me the BTST Plans")  

    message = get_message("select_plan").replace("{user_name}", user_first_name)
    await send_llm_response_line_by_line(message, update, context)
  
    contact_provided = await request_contact(update, context)
    if not contact_provided:
        context.chat_data['post_contact_action'] = 'ask_capital'
        return        
 
    await ask_for_capital(update, context)
    # message = f"""
    #     I need some more details to check if our plan is suitable for you ✅    
    # """
    # await send_llm_response_line_by_line(message, update, context)

    # await simulate_typing(context, chat_id, 2) 
    # message = f"Please select the capital you would like to invest in BTST trades 💰" 
    # await query.message.reply_text(
    #     message,
    #     reply_markup=reply_markup_capital
    # )   
    # save_message(chat_id, sender="bot", message=message)      
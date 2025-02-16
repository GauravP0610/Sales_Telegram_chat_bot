import time
from telegram import Update
from telegram.ext import  ContextTypes

from f_mongo_functions import save_message, save_user_detail
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.t_reply_markup_keyboards import  reply_markup_returns

async def handle_capital_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    user_first_name = query.from_user.first_name

    # Capture the user's selection
    user_selection = query.data  # callback_data value
    capital_mapping = {
        "capital_1lakh": "below 1 lakh",
        "capital_5lakh": "1 lakh to 5 lakh",
        "capital_20lakh": "5 lakh to 20 lakh",
        "capital_50lakh": "Above 20 lakh",
    }
    selected_option = capital_mapping.get(user_selection, "an unknown amount")

    save_message(chat_id, sender="user", message=f"Selected capital: {selected_option}")
    save_user_detail(chat_id, "user_capital", user_selection)

    message = f"""
        That's the right amount for BTST ✅
        One last question...
    """
    await send_llm_response_line_by_line(message, update, context)   

    message = f"How much monthly returns do you expect to make on your capital?"
    await query.message.reply_text(message, reply_markup = reply_markup_returns)
    save_message(chat_id, sender="bot", message=message)       

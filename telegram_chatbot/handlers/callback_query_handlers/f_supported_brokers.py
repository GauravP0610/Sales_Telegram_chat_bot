
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import  ContextTypes

from f_mongo_functions import save_message
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.t_reply_markup_keyboards import reply_markup_breakoutai


async def supported_brokers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    user_first_name = query.from_user.first_name

    await query.answer() 
    save_message(chat_id, sender="user", message="What brokers are supported by BreakoutAI")  

    message = f"""
        BreakoutAI currently supports 20 brokers in India 🇮🇳
        Here is the list of supported brokers:
        1️⃣ Fyers, 2️⃣ Alice Blue, 3️⃣ AN API, 4️⃣ Compositedge, 5️⃣ DhanHQ, 6️⃣ Finvasia, 7️⃣ Firstock, 8️⃣ Flattrade, 9️⃣ 5Paisa, 🔟 Goodwill, 1️⃣1️⃣ Kotak, 1️⃣2️⃣ Motilal Oswal, 1️⃣3️⃣ Paytm, 1️⃣4️⃣ Rupeezy, 1️⃣5️⃣ Samco, 1️⃣6️⃣ Tradejini, 1️⃣7️⃣ Upstox, 1️⃣8️⃣ Zebu, 1️⃣9️⃣ Zerodha.

    """
    await send_llm_response_line_by_line(message, update, context)
 
    await simulate_typing(context, chat_id, 5) 
    message = f"{user_first_name} Ji, how would you like to proceed? 😄 " 
    await query.message.reply_text(
        message,
        reply_markup=reply_markup_breakoutai
    )   
    save_message(chat_id, sender="bot", message=message)      
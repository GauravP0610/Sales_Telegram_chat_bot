import time
from telegram import Update
from telegram.ext import  ContextTypes

from f_mongo_functions import save_message, save_user_detail
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.t_reply_markup_keyboards import  reply_markup_whatsapp

async def make_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    user_first_name = query.from_user.first_name

    # Capture the user's selection
    user_selection = query.data  # callback_data value
    plans_mapping = {
        "plans_1": "1 month for ₹4990",
        "plans_2": "3 months for ₹9990 + 1 month extra free",
        "plans_3": "12 months for ₹20990",
        "plans_1_1": "1 month for ₹3990",
        "plans_1_2": "3 months for ₹6990 + 1 month extra free",
        "plans_1_3": "12 months for ₹10990",
        "plans_2_1": "1 month for ₹4990",
        "plans_2_2": "3 months for ₹9990 + 1 month extra free",
        "plans_2_3": "12 months for ₹20990",
        "plans_3_1": "1 month for ₹6890",
        "plans_3_2": "3 months for ₹14990 + 1 month extra free",
        "plans_3_3": "12 months for ₹29990",
        "plans_4_1": "1 month for ₹9990",
        "plans_4_2": "3 months for ₹19990 + 1 month extra free",
        "plans_4_3": "12 months for ₹40990",
    }

    selected_option = plans_mapping.get(user_selection, "an unknown amount")

    save_message(chat_id, sender="user", message=f"Selected capital: {selected_option}")
    save_user_detail(chat_id, "selected_plan", user_selection)

    message = f"""
        You have selected the plan : {selected_option} ✅
        1️⃣ Kindly transfer the amount on UPI to breakoutai@ybl
        2️⃣ Once the transfer is made, kindly send the payment screenshot on whatsapp: +91 95201 70220. 
        3️⃣ Your plan will be instantly activated after that and you will start receiving trades on Telegram.
    """
    await send_llm_response_line_by_line(message, update, context)    

    message = f"4️⃣ Click the button below to open whatsapp ✅"
    await query.message.reply_text(message, reply_markup = reply_markup_whatsapp)
    save_message(chat_id, sender="bot", message=message)   
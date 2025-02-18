import time
from telegram import Update
from telegram.ext import ContextTypes
from f_mongo_functions import save_message, save_user_detail, get_message
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.t_reply_markup_keyboards import reply_markup_whatsapp
from f_mongo_functions import get_keyboard_text

async def make_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    user_first_name = query.from_user.first_name

    # Capture the user's selection
    user_selection = query.data  # callback_data value
    plans_mapping = {
        "plans_1": get_keyboard_text("group_5", "18"),
        "plans_2": get_keyboard_text("group_5", "19"),
        "plans_3": get_keyboard_text("group_5", "20"),
        "plans_1_1": get_keyboard_text("group_6", "21"),
        "plans_1_2": get_keyboard_text("group_6", "22"),
        "plans_1_3": get_keyboard_text("group_6", "23"),
        "plans_2_1": get_keyboard_text("group_6", "24"),
        "plans_2_2": get_keyboard_text("group_6", "25"),
        "plans_2_3": get_keyboard_text("group_6", "26"),
        "plans_3_1": get_keyboard_text("group_7", "27"),
        "plans_3_2": get_keyboard_text("group_7", "28"),
        "plans_3_3": get_keyboard_text("group_7", "29"),
        "plans_4_1": get_keyboard_text("group_8", "30"),
        "plans_4_2": get_keyboard_text("group_8", "31"),
        "plans_4_3": get_keyboard_text("group_8", "32"),
    }

    selected_option = plans_mapping.get(user_selection, "an unknown amount")

    save_message(chat_id, sender="user", message=f"Selected capital: {selected_option}")
    save_user_detail(chat_id, "selected_plan", user_selection)

    message = get_message("make_payment_instruction").replace("{plan}", selected_option)
    await send_llm_response_line_by_line(message, update, context)    

    message = get_message("click_whatsapp")
    await query.message.reply_text(message, reply_markup = reply_markup_whatsapp)
    save_message(chat_id, sender="bot", message=message)
import time
from telegram import Update
from telegram.ext import  ContextTypes

from f_mongo_functions import get_user_details, save_message, save_user_detail
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.t_reply_markup_keyboards import  reply_markup_plans_1, reply_markup_plans_2, reply_markup_plans_3, reply_markup_plans_4

async def handle_returns_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    user_first_name = query.from_user.first_name

    # Capture the user's selection
    user_selection = query.data  # callback_data value
    returns_mapping = {
        "returns_5": "5%",
        "returns_15": "5 to 15%",
        "returns_30": "15 to 30%",
        "returns_40": "30%",
    }
    selected_option = returns_mapping.get(user_selection, "")

    save_message(chat_id, sender="user", message=f"Selected returns expectation: {selected_option}")
    save_user_detail(chat_id, "user_returns_expectations", user_selection)
    user_capital = get_user_details(chat_id).get("user_capital")
    plan_quoted = get_user_details(chat_id).get("plan_quoted")

    message = f"""
Amazing!
I can help you achieve even more than {selected_option} monthly returns ✅
Give me just few seconds to find the best plan for you... ⏳
Applying 50% discount on the plans...
Discount Applied!!! 🎉
Here are your discounted plans 🚀 

    """
    await send_llm_response_line_by_line(message, update, context)   

    if not plan_quoted:

        if user_capital == "capital_1lakh":
            reply_markup_plans = reply_markup_plans_1
            save_user_detail(chat_id, "plan_quoted", "plans_1")
        elif user_capital == "capital_5lakh":
            reply_markup_plans = reply_markup_plans_2
            save_user_detail(chat_id, "plan_quoted", "plans_2")
        elif user_capital == "capital_20lakh":
            reply_markup_plans = reply_markup_plans_3
            save_user_detail(chat_id, "plan_quoted", "plans_3")
        elif user_capital == "capital_50lakh":
            reply_markup_plans = reply_markup_plans_4
            save_user_detail(chat_id, "plan_quoted", "plans_4")  

    else:
        if plan_quoted == "plans_1":
            reply_markup_plans = reply_markup_plans_1
        elif plan_quoted == "plans_2":
            reply_markup_plans = reply_markup_plans_2
        elif plan_quoted == "plans_3":
            reply_markup_plans = reply_markup_plans_3
        elif plan_quoted == "plans_4": 
            reply_markup_plans = reply_markup_plans_4
    
    await simulate_typing(context, chat_id, 4)
    message = f"Please click on the plan ⏰"
    await query.message.reply_text(message, reply_markup = reply_markup_plans)
    save_message(chat_id, sender="bot", message=message)    

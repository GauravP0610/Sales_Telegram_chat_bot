
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import  ContextTypes

from telegram_chatbot.handlers.callback_query_handlers.f_breakoutai_details import breakoutai_details
from telegram_chatbot.handlers.callback_query_handlers.f_btst_details import btst_details
from telegram_chatbot.handlers.callback_query_handlers.f_btst_strategy import btst_strategy
from telegram_chatbot.handlers.callback_query_handlers.f_capital_selection import handle_capital_selection
from telegram_chatbot.handlers.callback_query_handlers.f_chat_kapil_mittal import chat_kapil_mittal
from telegram_chatbot.handlers.callback_query_handlers.f_make_payment import make_payment
from telegram_chatbot.handlers.callback_query_handlers.f_past_accuracy import past_accuracy
from telegram_chatbot.handlers.callback_query_handlers.f_plans_btst import plans_btst
from telegram_chatbot.handlers.callback_query_handlers.f_returns_selection import handle_returns_selection
from telegram_chatbot.handlers.callback_query_handlers.f_subscribe_breakoutai import subscribe_breakoutai
from telegram_chatbot.handlers.callback_query_handlers.f_subscription_plans import subscription_plans
from telegram_chatbot.handlers.callback_query_handlers.f_supported_brokers import supported_brokers
from telegram_chatbot.t_reply_markup_keyboards import reply_markup_main

async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()  

    handlers = {
            "breakoutai_details": breakoutai_details,
            "subscribe_breakoutai": subscribe_breakoutai,
            "btst_details": btst_details,
            "btst_strategy": btst_strategy,
            "plans_btst": plans_btst,
            "capital_1lakh": handle_capital_selection,
            "capital_5lakh": handle_capital_selection,
            "capital_20lakh": handle_capital_selection,
            "capital_50lakh": handle_capital_selection,
            "returns_5": handle_returns_selection,
            "returns_15": handle_returns_selection,
            "returns_30": handle_returns_selection,
            "returns_40": handle_returns_selection,
            "past_accuracy": past_accuracy,
            "subscription_plans": subscribe_breakoutai,
            "chat_kapil_mittal": chat_kapil_mittal,
            "more_details_breakoutai": subscribe_breakoutai,
            "supported_brokers": supported_brokers,
            "plans_1": make_payment,
            "plans_2": make_payment,
            "plans_3": make_payment,
            "plans_1_1": make_payment,
            "plans_1_2": make_payment,
            "plans_1_3": make_payment,
            "plans_2_1": make_payment,
            "plans_2_2": make_payment,
            "plans_2_3": make_payment,
            "plans_3_1": make_payment,
            "plans_3_2": make_payment,
            "plans_3_3": make_payment,
            "plans_4_1": make_payment,
            "plans_4_2": make_payment,
            "plans_4_3": make_payment
        }

    handler = handlers.get(query.data)
    if handler:
        await handler(update, context)
    else:
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text="Invalid choice. Please try again."
        )

from telegram.ext import  ContextTypes
from telegram import Update

from f_mongo_functions import save_message
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.t_reply_markup_keyboards import reply_markup_capital

async def ask_for_capital(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = update.effective_user
    user_first_name = user.first_name or "User"

    # Initial message
    await send_llm_response_line_by_line("I need more details to check best plan for you ✅", update, context)
    await simulate_typing(context, chat_id, 2)

    # Determine which message object to reply to
    if update.callback_query:
        message = update.callback_query.message
    else:
        message = update.message

    # Send capital selection
    await message.reply_text(
        "Please select your investment capital 💰",
        reply_markup=reply_markup_capital
    )
    save_message(chat_id, sender="bot", message="Asked for capital selection")

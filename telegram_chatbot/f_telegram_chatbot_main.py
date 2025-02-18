'''The main file where the bot instance is created and handlers are imported and added to the bot. The main file f_run_bot.py imports 
   the function telegram_chatbot_main from f_telegram_chatbot_main.py and calls it to run the bot. '''

from config import Config
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram_chatbot.handlers.f_ensure_contact import handle_contact
from telegram_chatbot.handlers.f_handle_callback_query import handle_callback_query
from telegram_chatbot.handlers.f_handle_message import handle_message
from telegram_chatbot.handlers.f_request_contact import request_contact
from telegram_chatbot.handlers.f_start_command import start_command



TELEGRAM_BOT_TOKEN =Config.BOT_TOKEN

def telegram_chatbot_main():
    print("code is running")

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.ALL, handle_message))
    application.add_handler(CallbackQueryHandler(handle_callback_query))
    application.add_handler(MessageHandler(filters.CONTACT, handle_contact))
    

    application.run_polling()



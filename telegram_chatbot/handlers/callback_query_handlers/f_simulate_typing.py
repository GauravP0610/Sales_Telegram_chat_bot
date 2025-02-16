import asyncio
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import CallbackQueryHandler, MessageHandler, ContextTypes
from telegram.ext import filters 

async def simulate_typing(context: ContextTypes.DEFAULT_TYPE, chat_id: int, duration: int = 3):
    """Simulates typing behavior by sending a 'typing...' action for a specified duration."""
    await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    await asyncio.sleep(duration)  # Wait for the duration to simulate typing



import time
from telegram.error import BadRequest
from f_mongo_functions import save_message
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
import random


async def send_llm_response_line_by_line(bot_raw_response, update, context):

    lines = bot_raw_response.split("\n")
    chat_id = update.effective_chat.id
    message_object = update.message or update.callback_query.message
    save_message(chat_id, "bot", bot_raw_response)

    for line in lines:
        # Skip empty lines
        if line.strip():
            time.sleep(1)
            random_delay = random.randint(1, 5)
            await simulate_typing(context, chat_id, random_delay)            
            try:
                await message_object.reply_text(line.strip(), parse_mode="Markdown")
            except BadRequest as e:
                if "can't parse entities" in str(e):  # Handle Markdown parsing issues
                    print(f"Markdown error detected. Retrying without Markdown. Error: {e}")
                    try:
                        # Retry without Markdown
                        await message_object.reply_text(line.strip())
                    except Exception as retry_error:
                        print(f"Retry without Markdown also failed. Error: {retry_error}")
                else:
                    raise


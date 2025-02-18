import re
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes
from f_mongo_functions import get_user_details, save_user_details, save_message, get_message
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_ask_for_capital import ask_for_capital
from f_llm_functions import generate_gemini_response

async def request_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_object = update.message or update.callback_query.message
    user = update.effective_user
    chat_id = update.effective_chat.id

    if context.chat_data.get('user_contact') or get_user_details(chat_id).get('phone_number'):
        return True

    if message_object.text:
        digits = re.sub(r'\D', '', message_object.text)
        if len(digits) < 10:
            await message_object.reply_text("Send a valid phone number (at least 10 digits).")
            return False
        
        prompt = f"Extract the phone number from this text: {message_object.text}"
        response = generate_gemini_response(prompt)
        extracted_number = re.sub(r'\D', '', response)
        
        if len(extracted_number) < 10:
            await message_object.reply_text("Could not extract a valid number. Please re-enter.")
            return False
        
        await message_object.reply_text(f"Verify this is your number: {extracted_number}")
        context.chat_data['awaiting_confirmation'] = extracted_number
        return False

    if context.chat_data.get('awaiting_confirmation'):
        if message_object.text.lower() == 'yes':
            phone_number = context.chat_data.pop('awaiting_confirmation')
            user_details = {
                "first_name": user.first_name,
                "last_name": user.last_name or "N/A",
                "username": user.username or "N/A",
                "language_code": user.language_code or "N/A",
                "is_premium": getattr(user, "is_premium", False),
                "phone_number": phone_number
            }
            save_user_details(chat_id, user_details)
            context.chat_data['user_contact'] = phone_number
            await send_llm_response_line_by_line("Your number has been verified.", update, context)
            return True
        else:
            await message_object.reply_text("Number not confirmed. Please enter again.")
            return False

    contact_button = KeyboardButton("Verify your phone number ✅", request_contact=True)
    contact_keyboard = ReplyKeyboardMarkup([[contact_button]], one_time_keyboard=True, resize_keyboard=True)
    message = get_message("request_contact")
    await message_object.reply_text(message, reply_markup=contact_keyboard)
    context.chat_data['awaiting_contact'] = True
    return False

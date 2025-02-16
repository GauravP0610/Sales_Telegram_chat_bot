import time
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from f_mongo_functions  import get_user_details, save_message, save_user_detail, save_user_details
from telegram_chatbot.f_llm_response_line import send_llm_response_line_by_line
from telegram_chatbot.handlers.callback_query_handlers.f_ask_for_capital import ask_for_capital
from telegram_chatbot.handlers.callback_query_handlers.f_simulate_typing import simulate_typing
from telegram_chatbot.t_reply_markup_keyboards import reply_markup_main, reply_markup_kapil 



async def request_contact(update, context):
    """
    Requests the user's contact information if not already provided.
    """
    message_object = update.message or update.callback_query.message
    user = update.effective_user
    chat_id = update.effective_chat.id
    user_first_name = user.first_name or "User"

    print("Debug: Context in request_contact:", context)
    print("Debug: Context.chat_data in request_contact:", getattr(context, "chat_data", None))    

    if context.chat_data.get('user_contact') or get_user_details(chat_id).get('phone_number'):
        return True

    # If awaiting contact and contact is shared
    if context.chat_data.get('awaiting_contact') and message_object.contact:
        contact = message_object.contact
        phone_number = contact.phone_number
        user = message_object.from_user
        user_details = {
            "first_name": user.first_name,
            "last_name": user.last_name or "N/A",  # Handle None values
            "username": user.username or "N/A",
            "language_code": user.language_code or "N/A",
            "is_premium": getattr(user, "is_premium", False),
            "phone_number": phone_number
        }

        save_user_details(chat_id, user_details)
        # Update chat_data to mark contact as provided
        context.chat_data['user_contact'] = phone_number
        context.chat_data.pop('awaiting_contact', None)  # Remove the awaiting flag

        message = f"""
            Verifying your phone number ... ⏳
        
            Thank you, {user.first_name} Ji 🙏! Your phone number is now verified ✅ \n\n           
        """
        await send_llm_response_line_by_line(message, update, context)
        post_action = context.chat_data.get('post_contact_action')
        if post_action == 'ask_capital':
            await ask_for_capital(update, context)
            del context.chat_data['post_contact_action']
        return True        

    # Request contact if not already provided
    if not context.chat_data.get('user_contact'):

        context.chat_data['awaiting_contact'] = True

        contact_button = KeyboardButton("Verify your phone number ✅", request_contact=True)
        contact_keyboard = ReplyKeyboardMarkup([[contact_button]], one_time_keyboard=True, resize_keyboard=True)

        message= f" Please click the button below ⬇️ "
        await message_object.reply_text(
            message,
            reply_markup=contact_keyboard
        )   
        save_message(chat_id, sender="bot", message=message)
        return False

    return True
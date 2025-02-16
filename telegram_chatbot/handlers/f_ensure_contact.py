from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import ContextTypes

from f_mongo_functions import save_message

async def ensure_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id

    # Check if the user has already shared their contact (assuming you have some way of verifying this)
    user_data = context.user_data.get("contact_shared", False)
    
    if not user_data:
        # Ask for the contact number
        await query.message.reply_text(
            "Please share your contact number to proceed 📱",
            reply_markup=ReplyKeyboardMarkup(
                [[KeyboardButton("Share Contact ☎️", request_contact=True)]],
                one_time_keyboard=True,
                resize_keyboard=True,
            ),
        )
        return False  # Indicate that the flow should pause until contact is shared
    
    return True  # Indicate that the user has already shared contact


async def handle_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    contact = update.message.contact

    if contact:
        # Save contact information in user_data
        context.user_data["contact_shared"] = True
        save_message(chat_id, sender="user", message=f"Contact shared: {contact.phone_number}")
        await update.message.reply_text("Thank you for sharing your contact! ✅")
    else:
        await update.message.reply_text("Failed to retrieve contact. Please try again.")

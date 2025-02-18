"""Using MongoDB to store and retrieve messages and user details."""

from common_imports import telegram_chats, datetime, telegram_faqs, telegram_display_messages, telegram_keyboard_text

def save_message(chat_id, sender, message=None, file=None):
    """
    Save a message or file metadata to the database.

    :param chat_id: Telegram chat ID
    :param sender: Either 'user' or 'bot'
    :param message: Text message (optional)
    :param file: Dictionary containing file metadata (optional)
    """
    chat_id = int(chat_id)
    entry = {
        "timestamp": datetime.now(),
        "sender": sender,
        "message": message,
        "file": file
    }
    telegram_chats.update_one(
        {"chat_id": chat_id},
        {"$push": {"messages": entry}},
        upsert=True  # Create document if it doesn't exist
    )

# def get_conversation(chat_id, limit=20):
#     chat_id = int(chat_id)
#     """
#     Retrieve the latest messages for a given chat_id.
#     :param chat_id: Telegram chat ID
#     :param limit: Number of messages to retrieve
#     """
#     chat = telegram_chats.find_one({"chat_id": chat_id})
#     if chat and "messages" in chat:
#         return chat["messages"][-limit:]  # Return last `limit` messages
#     return []

def get_conversation(chat_id, limit=20):
    chat_id = int(chat_id)

    chat = telegram_chats.find_one({"chat_id": chat_id})
    if chat and "messages" in chat:
        # Remove timestamps from each message
        messages = [{k: v for k, v in msg.items() if k != "timestamp"} for msg in chat["messages"][-limit:]]
        return messages
    return []



def get_user_details(chat_id):
    chat_id = int(chat_id)
    """
    Retrieve user details sub-document for a given chat_id.
    Returns an empty dict if user_details does not exist.
    """
    chat = telegram_chats.find_one({"chat_id": chat_id})
    if chat and "user_details" in chat:
        return chat["user_details"]
    return {}


def save_user_detail(chat_id, field_name, field_value):
    """
    Saves or updates a single field in the user_details sub-document.
    Example usage:
        save_user_detail(chat_id, "phone_number", "9876543210")

    """
    chat_id = int(chat_id)
    telegram_chats.update_one(
        {"chat_id": chat_id},
        {"$set": {f"user_details.{field_name}": field_value}},
        upsert=True  # Create or update the document
    )

def save_user_faq(chat_id, field_value):
    """
    Saves or updates a single field in the user_details sub-document.
    Example usage:
        save_user_detail(chat_id, "phone_number", "9876543210")

    """
    chat_id = int(chat_id)
    telegram_faqs.update_one(
        {"chat_id": chat_id},
        {"$push": {"faq": field_value}},
        upsert=True  # Create or update the document
    )    

def save_user_details(chat_id, user_details):
    """
    Saves or updates all user details in the user_details sub-document.
    Example usage:
        save_user_details(chat_id, {
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "language_code": "en",
            "is_premium": True
        })
    """
    chat_id = int(chat_id)  # Ensure chat_id is always an integer
    telegram_chats.update_one(
        {"chat_id": chat_id},
        {"$set": {"user_details": user_details}},  # Update the entire user_details sub-document
        upsert=True  # Create the document if it doesn't exist
    )

  
# To get display messages from the collection telegram_display_messages

def get_message(message_id):
    """
    Retrieve a message from the messages collection.
    :param message_id: The ID of the message to retrieve.
    :return: The message text or a default message if not found.
    """
    message = telegram_display_messages.find_one({"_id": message_id})
    return message["text"] if message else "Message not found."

# To get keyboard buttons from the collection telegram_keyboard_text

def get_keyboard_text(group_id, button_id):
    """
    Retrieve a keyboard button text from the keyboard_text collection.
    :param group_id: The ID of the group to search.
    :param button_id: The ID of the button to retrieve within the group.
    :return: The button text or a default message if not found.
    """
    group = telegram_keyboard_text.find_one({"_id": group_id})
    if group and "buttons" in group:
        for button in group["buttons"]:
            if button["_id"] == button_id:
                return button["text"]
    return "Button not found."

# Example usage:
# text = get_keyboard_text("group_1", "1")





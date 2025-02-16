import requests
from common_imports import telegram_chats
from f_mongo_functions import save_message


def send_messages_to_all_users(bot_token, message_text):

    users = telegram_chats.find({})
    telegram_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    for user in users:
        chat_id = user.get('chat_id')
        user_details = user.get('user_details')
        if chat_id:
            if not user_details:
                response = requests.post(
                    telegram_api_url,
                    data={
                        "chat_id": chat_id,
                        "text": message_text
                    }
                )
                save_message(chat_id, "bot", message=message_text)
            
                if response.status_code == 200:
                    print(f"Message sent to chat_id {chat_id}")
                    save_message(chat_id, "bot", message=message_text)
                else:
                    error_data = response.json()  # Extract JSON response
                    if error_data.get("error_code") == 403:  # Bot blocked by the user
                        print(f"Failed to send message to chat_id {chat_id}: {error_data.get('description')}")
                        # Update the user's details in the database
                        telegram_chats.update_one(
                            {"chat_id": chat_id},
                            {"$set": {
                                "user_details.is_blocked": True,
                                "user_details.error_description": error_data.get("description")
                            }}
                        )
                    else:
                        print(f"Failed to send message to chat_id {chat_id}: {response.text}")
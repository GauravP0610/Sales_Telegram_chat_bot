from datetime import datetime
import requests
from common_imports import telegram_chats
from f_mongo_functions import save_message


def select_plan_loop(bot_token):

    users = telegram_chats.find({})
    telegram_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"


    
    for user in users:
        chat_id = user.get('chat_id')
        user_details = user.get('user_details')
        if not user_details:  # Skip if user_details is missing
            print(f"Skipping user with chat_id {chat_id} due to missing user_details.")
            continue

        selected_plan = user_details.get('selected_plan')
        plan_quoted = user_details.get('plan_quoted')
        is_blocked = user_details.get('is_blocked', False) 
        user_name = user_details.get('first_name', 'Investor')
        if chat_id:
            if plan_quoted and not selected_plan and not is_blocked:

                message = f"""🔥 Your BTST trades are waiting! 🔥
                {user_name} Ji, you haven’t selected a plan yet! 📌
                Choose a plan right now before the market closes ⏰
                ⚡ Limited spots available!.
                """                
                response = requests.post(
                    telegram_api_url,
                    data={
                        "chat_id": chat_id,
                        "text": message
                    }
                )
                save_message(chat_id, "bot", message=message)
            
                if response.status_code == 200:

                    followup_entry = {
                        "date": datetime.now(),
                        "reason": "User has not selected a plan after being quoted"
                    }

                    # Append follow-up entry to the array
                    telegram_chats.update_one(
                        {"chat_id": chat_id},
                        {"$push": {"user_details.followups": followup_entry}}
                    )                    
                else:
                    error_data = response.json()  # Extract JSON response
                    if error_data.get("error_code") == 403:  # Bot blocked by the user
                        print(f"Failed to send message to chat_id {chat_id}: {error_data.get('description')}")
                        save_message(chat_id, "user", message=error_data.get('description'))
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
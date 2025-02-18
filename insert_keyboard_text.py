# Insert keyboard text in the database

from common_imports import telegram_keyboard_text

# Define messages
messages = [
    {"_id": "1", "text": "🤖 BreakoutAI"},
    {"_id": "2", "text": "💹 BTST Calls"},
    {"_id": "3", "text": "💯 Past Accuracy"},
    {"_id": "4", "text": "🤩 Subscription Plans"},
    {"_id": "5", "text": "Chat with Kapil Mittal"},
    {"_id": "6", "text": "Plans: Get 50% discount 🎉"},
    {"_id": "7", "text": "Supported Brokers"},
    {"_id": "8", "text": "BTST Strategy"},
    {"_id": "9", "text": "Plans: Get 50% discount ⏰"},
    {"_id": "10", "text": "below 1 lakh"},
    {"_id": "11", "text": "1 lakh to 5 lakh"},
    {"_id": "12", "text": "5 lakh to 20 lakh"},
    {"_id": "13", "text": "Above 20 lakh"},
    {"_id": "14", "text": "upto 5%"},
    {"_id": "15", "text": "5 to 15%"},
    {"_id": "16", "text": "15 to 30%"},
    {"_id": "17", "text": "more than 30%"},
    {"_id": "18", "text": "1 month for ₹4990"},
    {"_id": "19", "text": "3 months for ₹9990 + 1 month extra free"},
    {"_id": "20", "text": "12 months for ₹20990"},
    {"_id": "21", "text": "1 month for ₹3990"},
    {"_id": "22", "text": "3 months for ₹6990 + 1 month extra free"},
    {"_id": "23", "text": "12 months for ₹10990"},
    {"_id": "24", "text": "1 month for ₹4990"},
    {"_id": "25", "text": "3 months for ₹9990 + 1 month extra free"},
    {"_id": "26", "text": "12 months for ₹20990"},
    {"_id": "27", "text": "1 month for ₹6890"},
    {"_id": "28", "text": "3 months for ₹14990 + 1 month extra free"},
    {"_id": "29", "text": "12 months for ₹29990"},
    {"_id": "30", "text": "1 month for ₹9990"},
    {"_id": "31", "text": "3 months for ₹19990 + 1 month extra free"},
    {"_id": "32", "text": "12 months for ₹40990"},
    {"_id": "33", "text": "Fyers: Verfied PnL"},
    {"_id": "34", "text": "Zerodha: Verfied PnL"},
    {"_id": "35", "text": "Video on BreakoutAI accuracy"},
    {"_id": "36", "text": "Send to whatsapp 😄"},
    {"_id": "37", "text": "Back to Main Menu"},
    {"_id": "38", "text": "Chat with Kapil Mittal"},
]

# Group messages into arrays
grouped_messages = [
    {"_id": "group_1", "buttons": messages[0:5]},
    {"_id": "group_2", "buttons": messages[5:8]},
    {"_id": "group_3", "buttons": messages[8:12]},
    {"_id": "group_4", "buttons": messages[12:16]},
    {"_id": "group_5", "buttons": messages[16:20]},
    {"_id": "group_6", "buttons": messages[20:24]},
    {"_id": "group_7", "buttons": messages[24:28]},
    {"_id": "group_8", "buttons": messages[28:32]},
    {"_id": "group_9", "buttons": messages[32:36]},
    {"_id": "group_10", "buttons": messages[36:38]},
]

# Insert grouped messages into MongoDB
for group in grouped_messages:
    telegram_keyboard_text.update_one({"_id": group["_id"]}, {"$set": group}, upsert=True)

print("Grouped messages inserted successfully!")
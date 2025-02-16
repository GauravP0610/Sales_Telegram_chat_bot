import pymongo
from pymongo import MongoClient
from collections import defaultdict
from dateutil import parser
import pandas as pd
import schedule
import time
from datetime import datetime, timezone
from common_imports import telegram_chats, telegram_analytics


def get_new_chats(collection):
    """
    Retrieve chats where 'chat_counted' is not True.
    """
    projection = {"messages": 1}
    return collection.find({}, projection)

def update_counts(counts_collection, hour_counts, field_name):
    """
    Replace chat counts instead of incrementing them.
    """
    updated_data = [{"hour": hour, "message_count": count} for hour, count in hour_counts.items()]
    
    counts_collection.update_one(
        {"_id": "chat_counts_bot"},
        {"$set": {field_name: updated_data}},
        upsert=True
    )

def update_daily_counts(counts_collection, daily_chat_counts):
    """
    Replace daily chat counts in MongoDB.
    """
    counts_collection.update_one(
        {"_id": "chat_counts_bot"},
        {"$set": {"total_chat_counts_per_day_bot": daily_chat_counts}},
        upsert=True
    )



def bot_chat_counts():
    """
    The main job to be run daily.
    """
    print(f"Job started at {datetime.now()} UTC")

    chats_collection = telegram_chats
    counts_collection = telegram_analytics

    cursor = get_new_chats(chats_collection)
    hour_counts = defaultdict(int)
    first_message_counts = defaultdict(int)
    daily_chat_counts = defaultdict(int)

    for doc in cursor:
        messages = doc.get("messages", [])
        first_message_hour = None
        first_message_date = None
        for message in messages:
            if message.get("sender") == "bot":
                timestamp = message.get("timestamp")
                if timestamp:
                    try:
                        if isinstance(timestamp, str):
                            # Parse the timestamp string to a datetime object
                            timestamp = parser.isoparse(timestamp)                        
                        # Parse the timestamp string to a datetime object
                        elif isinstance(timestamp, datetime):
                            # Ensure the timestamp is timezone-aware
                            if timestamp.tzinfo is None:
                                timestamp = timestamp.replace(tzinfo=timezone.utc)
                        else:
                            raise ValueError(f"Unsupported timestamp type: {type(timestamp)}")
                        # Extract the hour (0-23) in UTC
                        if timestamp.tzinfo:
                            timestamp = timestamp.astimezone(timezone.utc)
                        else:
                            timestamp = timestamp.replace(tzinfo=timezone.utc)                        
                        hour = timestamp.hour
                        date = timestamp.date().isoformat()
                        hour_counts[hour] += 1

                        # Track the first user message per chat
                        if first_message_hour is None:
                            first_message_hour = hour
                            first_message_counts[first_message_hour] += 1 

                        if first_message_date is None:
                            first_message_date = date
                            daily_chat_counts[first_message_date] += 1                             

                    except Exception as e:
                        print(f"Error parsing timestamp {timestamp}: {e}")

    if hour_counts or first_message_counts or daily_chat_counts:
        # Update the counts in the counts collection
        update_counts(counts_collection, hour_counts, "chat_counts_bot")
        update_counts(counts_collection, first_message_counts, "bot_chat_counts_first_message")
        update_daily_counts(counts_collection, daily_chat_counts)        

        print("Hourly counts updated:", dict(hour_counts))
        print("First message hourly counts updated:", dict(first_message_counts))        # Mark chats as counted
        print("Daily chat counts updated:", dict(daily_chat_counts))

    else:
        print("No new chats to process.")

    print(f"Job finished at {datetime.now()} UTC\n")



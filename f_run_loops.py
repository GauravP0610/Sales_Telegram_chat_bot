from config import Config
import time
import schedule
from telegram_chatbot.analytics.f_chat_count_analytics_bot import bot_chat_counts
from telegram_chatbot.analytics.f_chat_count_analytics_user import user_chat_counts
from telegram_chatbot.followup_functions.f_select_plan_loop import select_plan_loop

# Get the bot token from environment variables
TELEGRAM_BOT_TOKEN = Config.BOT_TOKEN

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("Error: BOT_TOKEN environment variable is not set!")

def select_plan_nudge():
    """Run the daily plan selection nudge function."""
    print("Running daily select_plan_loop...")
    try:
        select_plan_loop(TELEGRAM_BOT_TOKEN)
        print("select_plan_loop executed successfully.")
    except Exception as e:
        print(f"Error in select_plan_loop: {e}")

def chat_counts():
    """Run chat count analytics functions."""
    print("Running daily chat_counts job...")
    try:
        bot_chat_counts()
        user_chat_counts()
        print("Chat count analytics executed successfully.")
    except Exception as e:
        print(f"Error in chat_counts job: {e}")

# Schedule the jobs
schedule.every().day.at("09:00").do(select_plan_nudge)
schedule.every().day.at("00:00").do(chat_counts)

print("Scheduler started. Waiting for the next scheduled task...")

# Keep the script running
try:
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every 60 seconds
except KeyboardInterrupt:
    print("Scheduler stopped. Exiting gracefully.")

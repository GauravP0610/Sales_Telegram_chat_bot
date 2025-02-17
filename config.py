import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    MONGO_URI = os.getenv('MONGODB_ATLAS_URI')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    SEARCH_API_KEY = os.getenv('SERPAPI_KEY')
    DATABASE_NAME = "telegram_bot"
    DB_NAME_BREAKOUT=os.getenv("DB_NAME_BREAKOUT")
    DB_NAME_USER=os.getenv("DB_NAME_USER")
    DB_NAME_CHATBOT=os.getenv("DB_NAME_CHATBOT")

from config import Config
Config.BOT_TOKEN
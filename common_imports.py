from config import Config
from pymongo import MongoClient, UpdateOne, errors
import os
from datetime import datetime


CONNECTION_STRING = Config.MONGO_URI
client = MongoClient(CONNECTION_STRING)
db = client['breakout']
db_user = client['user_details']
db_chatbot = client['telegram_chatbot']

telegram_chats = db_user["user_chats"]
telegram_faqs = db_user["telegram_faqs"]
telegram_analytics = db_chatbot["telegram_analytics"]
gemini_model = "gemini-1.5-flash"
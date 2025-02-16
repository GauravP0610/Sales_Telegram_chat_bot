
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import  ContextTypes


async def subscription_plans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() 
    
    time.sleep(1)
    
    await query.message.reply_text(
        f"I am BreakoutAI, trained in Germany 🇩🇪 built for India 🇮🇳 "
    )    

    await context.bot.send_message(
        chat_id=query.message.chat_id,
        text="We offer flexible subscription plans. Visit our website for more details.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")],
            [InlineKeyboardButton("Chat with Kapil Mittal", callback_data="chat_kapil_mittal")]
        ])
    )    


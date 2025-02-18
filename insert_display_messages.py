# Insert display messages in the database

from common_imports import telegram_display_messages

# Define messages
messages = [
    {"_id": "welcome_message", "text": "Welcome! {user_first_name} Ji 🙏 I am Kapil Mittal, hedge fund manager in Germany 🇩🇪 and #1 stock analyst on Tradingview!"},
    {"_id": "welcome_back_message", "text": "{user_first_name} Ji, what can I help you with today? 😄"},
    {"_id": "ask_contact", "text": "Please share your contact number to proceed 📱"},
    {"_id": "verify_contact", "text": "Thank you, {user_first_name} Ji 🙏! Your phone number is now verified ✅"},
    {"_id": "select_plan", "text": "🔥 Your BTST trades are waiting! Choose a plan before the market closes ⏰"},
    {"_id": "investment_capital", "text": "How much capital do you have to invest? There is NO minimum capital requirement for BreakoutAI!💰"},
    {"_id": "plan_selection_prompt", "text": "Please select your investment capital 💰"},
    {"_id": "ask_returns", "text": "How much monthly returns do you expect to make on your capital?"},
    {"_id": "discount_message", "text": "Applying 50% discount on the plans... Discount Applied!!! 🎉 Here are your discounted plans 🚀"},
    {"_id": "make_payment_instruction", "text": "You have selected the plan: {plan} ✅ 1️⃣ Kindly transfer the amount on UPI to breakoutai@ybl. 2️⃣ Once the transfer is made, kindly send the payment screenshot on WhatsApp: +91 95201 70220. 3️⃣ Your plan will be activated instantly!"},
    {"_id": "chat_connected", "text": "You are now connected! Please ask your questions ✅"},
    {"_id": "ask_subscription", "text": "I want to subscribe to BreakoutAI"},
    {"_id": "bot_typing", "text": "Connecting your chat with Kapil Mittal, please wait... ⏳"},
    {"_id": "past_accuracy_info", "text": "Great that you asked! {user_first_name} Ji, I am the only analyst in the markets who shares his verified PnL transparently."},
    {"_id": "supported_brokers_info", "text": """ BreakoutAI currently supports 20 brokers in India 🇮🇳
Here is the list of supported brokers:
1️⃣ Fyers, 2️⃣ Alice Blue, 3️⃣ AN API, 4️⃣ Compositedge, 5️⃣ DhanHQ, 6️⃣ Finvasia, 7️⃣ Firstock, 8️⃣ Flattrade, 9️⃣ 5Paisa, 🔟 Goodwill, 1️⃣1️⃣ Kotak, 1️⃣2️⃣ Motilal Oswal, 1️⃣3️⃣ Paytm, 1️⃣4️⃣ Rupeezy, 1️⃣5️⃣ Samco, 1️⃣6️⃣ Tradejini, 1️⃣7️⃣ Upstox, 1️⃣8️⃣ Zebu, 1️⃣9️⃣ Zerodha."""},
    {"_id": "here_are_the_links", "text": "Here are the links 👇"},
    {"_id": "eligible_for_discount", "text": "Congratulations {user_first_name} Ji 🎉, you are eligible for 50% extra discount on BTST plans! 👇"},
    {"_id": "analyst_verified_pnl", "text": "{user_first_name} Ji, I am the only analyst in the markets who share his verified PnL transparently."},
    {"_id": "services_offered", "text": "Services offered by me: ⬇️"},
    {"_id": "fallback_reply", "text": "Sorry I am currently unavailable on Telegram. You can reach out to me on whatsapp: tinyurl.com/whatsappbreakout"},
    {"_id": "how_would_you_like_to_proceed", "text": "{user_first_name} Ji, how would you like to proceed? 😄"},
    {"_id": "file_received", "text": "Thanks! I’ve received your file: {file_name}"},
    {"_id": "photo_received", "text": "Thanks for the photo! I’ve received it."},
    {"_id": "click_whatsapp", "text": "4️⃣ Click the button below to open whatsapp ✅"},
    {"_id": "breakoutai_details", "text": """Great let me share some details about BreakoutAI!

Gaurav Ji, BreakoutAI is India's first AI trading solution. It is built in Germany 🇩🇪 and trained in India 🇮🇳.

It scans 2000+ stocks every second to predict the future stock prices and helps you make profits in the stock markets. 🚀.

If you connect your broker (eg. Fyers, Upstox, Zerodha, ICICI), BreakoutAI will automatically buy and sell highly profitable stocks on your account!

It is 100% safe and secure ✅

If you are not comfortable with connecting your broker, you can opt for manual calls also!"""},
    {"_id": "subscription_plans", "text": "We offer flexible subscription plans. Visit our website for more details."},
    {"_id": "you_can_click_on_the_link_below", "text": "You can click on the link below to see my verified PnL from Zerodha or Fyers."},
    {"_id": "btst_details", "text": """Everyday I will send you 5 BTST stocks to trade at 2:30 PM ⏱️.
You buy these BTST stocks anytime before 3:30 PM 
Next day we sell the stocks at the provided Target and make profits! 🚀         
Each stock will have exact Target and SL for next day ✅
{user_first_name} Ji, you make 3-5% in profits everyday with BTST trades."""},
    {"_id": "btst_strategy", "text": """{user_first_name} Ji, I have spent last 6 years to develop a highly successful BTST strategy. 👨🏻‍💻
These kinds of strategies have always been hidden from small traders.
I have achieved 95% accuracy with this strategy! 💯
My goal is to help traders in the market by letting you use these profitable strategies to make money! 😄
I suggest only highly liquid stocks so the strategy works even when markets are falling. ✅
I spend more than 5 hours every day analyzing charts to find the best BTST trades for you! 🚀"""},
    {"_id": "finding_best_plan", "text": """Finding the best plan for you ⏳
{user_first_name} Ji, I need some more details to find the right plan for you ✅"""},
    {"_id": "how_much_capital", "text": "How much Capital do you have to invest? There is NO minimum capital requirement for BreakoutAI!💰"},
    {"_id": "right_amount_btst", "text": "That's the right amount for BTST ✅ One last question..."},
    {"_id": "connecting_chat", "text": "Connecting your chat with Kapil Mittal, please wait... ⏳"},
    {"_id": "verify_phone_number", "text": """Verifying your phone number ... ⏳
Thank you, {user_first_name} Ji 🙏! Your phone number is now verified ✅ \n\n"""},
    {"_id": "request_contact", "text": "Please click the button below ⬇️"},
    {"_id": "discount_applied", "text": """Amazing!
I can help you achieve even more than {selected_option} monthly returns ✅
Give me just few seconds to find the best plan for you... ⏳
Applying 50% discount on the plans...
Discount Applied!!! 🎉
Here are your discounted plans 🚀"""},
    {"_id": "click_plan", "text": "Please click on the plan ⏰"}
]

# Insert or update messages in the database
for message in messages:
    telegram_display_messages.update_one({"_id": message["_id"]}, {"$set": message}, upsert=True)

print("Messages inserted successfully!")
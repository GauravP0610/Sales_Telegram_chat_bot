from telegram import InlineKeyboardButton, InlineKeyboardMarkup


main_keyboard = [
    [InlineKeyboardButton("🤖 BreakoutAI", callback_data="breakoutai_details")],
    [InlineKeyboardButton("💹 BTST Calls", callback_data="btst_details")],
    [InlineKeyboardButton("💯 Past Accuracy", callback_data="past_accuracy")],
    [InlineKeyboardButton("🤩 Subscription Plans", callback_data="plans_btst")],
    [InlineKeyboardButton("Chat with Kapil Mittal", callback_data="chat_kapil_mittal")],
]
reply_markup_main = InlineKeyboardMarkup(main_keyboard)

chat_keyboard = [
    [InlineKeyboardButton("Chat with Kapil Mittal", callback_data="chat_kapil_mittal")],
]
reply_markup_kapil = InlineKeyboardMarkup(chat_keyboard)


breakoutai_keyboard = [
    [InlineKeyboardButton("BTST Calls", callback_data="btst_details")],
    [InlineKeyboardButton("Plans: Get 50% discount 🎉", callback_data="plans_btst")],
    [InlineKeyboardButton("Supported Brokers", callback_data="supported_brokers")],
]
reply_markup_breakoutai = InlineKeyboardMarkup(breakoutai_keyboard)

btst_keyboard = [
    [InlineKeyboardButton("BTST Strategy", callback_data="btst_strategy")],
    [InlineKeyboardButton("Plans: Get 50% discount 🎉", callback_data="plans_btst")],
]
reply_markup_btst = InlineKeyboardMarkup(btst_keyboard)

btst_strategy_keyboard = [
    [InlineKeyboardButton("Plans: Get 50% discount ⏰", callback_data="plans_btst")],
]
reply_markup_btst_strategy = InlineKeyboardMarkup(btst_strategy_keyboard)



capital_keyboard = [
    [InlineKeyboardButton("below 1 lakh", callback_data="capital_1lakh")],
    [InlineKeyboardButton("1 lakh to 5 lakh", callback_data="capital_5lakh")],
    [InlineKeyboardButton("5 lakh to 20 lakh", callback_data="capital_20lakh")],
    [InlineKeyboardButton("Above 20 lakh", callback_data="capital_50lakh")],
]
reply_markup_capital = InlineKeyboardMarkup(capital_keyboard)


returns_keyboard = [
    [InlineKeyboardButton("upto 5%", callback_data="returns_5")],
    [InlineKeyboardButton("5 to 15%", callback_data="returns_15")],
    [InlineKeyboardButton("15 to 30%", callback_data="returns_30")],
    [InlineKeyboardButton("more than 30%", callback_data="returns_40")],
]
reply_markup_returns = InlineKeyboardMarkup(returns_keyboard)

plans_keyboard = [
    [InlineKeyboardButton("1 month for ₹4990", callback_data="plans_1")],
    [InlineKeyboardButton("3 months for ₹9990 + 1 month extra free", callback_data="plans_2")],
    [InlineKeyboardButton("12 months for ₹20990", callback_data="plans_3")],
]
reply_markup_plans = InlineKeyboardMarkup(plans_keyboard)

plans_keyboard1 = [
    [InlineKeyboardButton("1 month for ₹3990", callback_data="plans_1_1")],
    [InlineKeyboardButton("3 months for ₹6990 + 1 month extra free", callback_data="plans_1_2")],
    [InlineKeyboardButton("12 months for ₹10990", callback_data="plans_1_3")],
]
reply_markup_plans_1 = InlineKeyboardMarkup(plans_keyboard1)

plans_keyboard2 = [
    [InlineKeyboardButton("1 month for ₹4990", callback_data="plans_2_1")],
    [InlineKeyboardButton("3 months for ₹9990 + 1 month extra free", callback_data="plans_2_2")],
    [InlineKeyboardButton("12 months for ₹20990", callback_data="plans_2_3")],
]
reply_markup_plans_2 = InlineKeyboardMarkup(plans_keyboard2)

plans_keyboard3 = [
    [InlineKeyboardButton("1 month for ₹6890", callback_data="plans_3_1")],
    [InlineKeyboardButton("3 months for ₹14990 + 1 month extra free", callback_data="plans_3_2")],
    [InlineKeyboardButton("12 months for ₹29990", callback_data="plans_3_3")],
]
reply_markup_plans_3 = InlineKeyboardMarkup(plans_keyboard3)

plans_keyboard4 = [
    [InlineKeyboardButton("1 month for ₹9990", callback_data="plans_4_1")],
    [InlineKeyboardButton("3 months for ₹19990 + 1 month extra free", callback_data="plans_4_2")],
    [InlineKeyboardButton("12 months for ₹40990", callback_data="plans_4_3")],
]
reply_markup_plans_4 = InlineKeyboardMarkup(plans_keyboard4)


verified_links_keyboard = [
    [InlineKeyboardButton("Fyers: Verfied PnL", url="tinyurl.com/fyerspnl")],
    [InlineKeyboardButton("Zerodha: Verfied PnL", url="tinyurl.com/zerodhapnl")],
    [InlineKeyboardButton("Video on BreakoutAI accuracy", url="tinyurl.com/breakoutaidemo")],
]
reply_markup_past_accuracy = InlineKeyboardMarkup(verified_links_keyboard)
    

whatsapp_keyboard = [
    [InlineKeyboardButton("Send to whatsapp 😄", url="tinyurl.com/whatsappbreakout")],
]
reply_markup_whatsapp = InlineKeyboardMarkup(whatsapp_keyboard)    
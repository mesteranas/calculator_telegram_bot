import message,app
import telegram
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import CommandHandler,MessageHandler,filters,ApplicationBuilder,CallbackQueryHandler
with open("token.bot","r",encoding="utf-8") as file:
    bot=ApplicationBuilder().token(file.read()).build()
async def start(update,contextt):
    info=update.effective_user
    keyboard=InlineKeyboardMarkup([[InlineKeyboardButton("donate",url="https://www.paypal.me/AMohammed231")],[InlineKeyboardButton("help",callback_data="help")]])
    await message.Sendmessage(chat_id=info.id,text="welcome " + str(info.first_name) + "to this bot. please send the math obration",reply_markup=keyboard)
async def handleMessages(update,context):
    info=update.effective_user
    try:
        result=eval(update.message.text)
    except:
        result="error"
    await message.Sendmessage(info.id,"result= " + str(result))
async def helb(update,contextt):
    links="""<a href="https://t.me/mesteranasm">telegram</a>

<a href="https://t.me/tprogrammers">telegram channel</a>

<a href="https://x.com/mesteranasm">x</a>

<a href="https://Github.com/mesteranas">Github</a>

email:
anasformohammed@gmail.com

<a href="https://Github.com/mesteranas/calculator_telegram_bot">visite project on Github</a>
"""
    info=update.effective_user
    await message.Sendmessage(info.id,"""name: {}\nversion: {}\ndescription: {}\n developer: {}\n contect us {}""".format(app.name,str(app.version),app.description,app.developer,links))
async def callBake(update,contextt):
    q=update.callback_query
    q.answer()
    if q.data=="help":
        await helb(update,contextt)

print("running")
bot.add_handler(CommandHandler("start",start))
bot.add_handler(CommandHandler("help",helb))
bot.add_handler(MessageHandler(filters.TEXT,handleMessages))
bot.add_handler(CallbackQueryHandler(callBake))
bot.run_polling()
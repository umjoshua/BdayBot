from dotenv import load_dotenv
import os
from telegram.ext import *
from handlers import handlers
import threading
import time
import datetime as dt
import sqlite3
import asyncio

load_dotenv()

async def cancel(update, context):
    await update.message.reply_text("Cancelled!")
    return ConversationHandler.END

application = Application.builder().token(os.getenv("TOKEN")).build()
application.add_handler(CommandHandler("start", handlers.start))

convHandler = application.add_handler(ConversationHandler(
    entry_points=[
        CommandHandler("new", handlers.newReminder),
        CommandHandler("view", handlers.viewReminders)
    ],
    states={
        1: [MessageHandler(filters.TEXT, handlers.getName)],
        2: [MessageHandler(filters.TEXT, handlers.getDate)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
))



async def remind():
    global application
    conn = sqlite3.connect("database/database.db")
    cursor = conn.cursor()
    while True:
        today = dt.date.today().strftime("%d-%m")
        print(today)
        cursor.execute("SELECT * FROM birthday_reminder WHERE date = ?",(str(today),))
        conn.commit()
        res = cursor.fetchall()
        for row in res:
            chatId = row[3]
            bdayName = row[2]
            text = "Hey! It's "+ bdayName + "'s birthday today... Wish him!"
            await application.updater.bot.send_message(chat_id=chatId,text=text)
        time.sleep(10)

def run_remind(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(remind())

new_loop = asyncio.new_event_loop()
t = threading.Thread(target=run_remind, args=(new_loop,))
t.start()

application.run_polling()
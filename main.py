from dotenv import load_dotenv
import os
from telegram.ext import *
from handlers import handlers
import threading
import time
import datetime as dt
import sqlite3

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


def remind():
    conn = sqlite3.connect("database/database.db")
    cursor = conn.cursor()
    while True:
        # time.sleep(60*60*24)
        today = dt.date.today().strftime("%d-%m")
        print(today)
        cursor.execute("SELECT * FROM birthday_reminder WHERE date = ?",(str(today),))
        conn.commit()
        res = cursor.fetchall()
        for row in res:
            print(row)
        time.sleep(1000)


remindThread = threading.Thread(target=remind)
remindThread.start()

application.run_polling()
import sqlite3
import datetime as dt
import time
import asyncio
from telegram.ext import *
import os
from dotenv import load_dotenv

load_dotenv()

application = Application.builder().token(os.getenv("TOKEN")).build()

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

asyncio.run(remind())
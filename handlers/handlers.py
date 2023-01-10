import sqlite3
from telegram.ext import ConversationHandler

startMessage = """
    Welcome!
    /new : create new reminder
    /view : view reminder
"""
new = "Whose birthday should I remember?"

conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

name = None
date = None
chatId = None

def setMonth(num):
    match(num):
        case 1:
            return 'January'
        case 2:
            return 'February'
        case 11:
            return 'November'


async def start(update, context):
    global chatId
    await update.message.reply_text(startMessage)
    chatId = update.message.chat_id
    res = cursor.execute("SELECT * FROM users where userId  = ?", (chatId, ))
    if not res.fetchone():
        cursor.execute("INSERT INTO users VALUES (?)", (chatId,))


async def newReminder(update, context):
    await update.message.reply_text("Whose birthday should I remember?")
    return 1


async def getName(update, context):
    global name
    name = update.message.text
    await update.message.reply_text("Enter DOB. (DD-MM)")
    return 2


async def getDate(update, context):
    global date
    date = update.message.text
    try:
        cursor.execute(
            "INSERT INTO birthday_reminder (date, name, flag, userId) VALUES(?,?,?,?)", (date, name, 0, chatId))
        conn.commit()
    except:
        await update.message.reply_text("Couldn't add. Start over with /start")
    else:
        await update.message.reply_text("I will remind you!")
    return ConversationHandler.END


async def viewReminders(update, context):
    global chatId
    chatId = update.message.chat_id
    cursor.execute("SELECT * FROM birthday_reminder where userId=?", (chatId,))
    conn.commit()
    res = cursor.fetchall()
    text = ""
    for row in res:
        text += "Name: " + row[2] + " DOB: " + row[1][0:2] + " " + setMonth(int(row[1][3:])) + "\n"
    await update.message.reply_text(text)

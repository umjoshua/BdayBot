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
    if num == '01':
        return 'January'
    elif num == '02':
        return 'February'
    elif num == '03':
        return 'March'
    elif num == '04':
        return 'April'
    elif num == '05':
        return 'May'
    elif num == '06':
        return 'June'
    elif num == '07':
        return 'July'
    elif num == '08':
        return 'August'
    elif num == '09':
        return 'September'
    elif num == '10':
        return 'October'
    elif num == '11':
        return 'November'
    elif num == '12':
        return 'December'
    else:
        return 'Invalid'


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
            "INSERT INTO birthday_reminder (date, name, userId) VALUES(?,?,?)", (date, name, chatId))
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
        text += row[2] + " - "  +  setMonth(row[1][3:]) + " " + row[1][0:2] + "\n"
    if text!="":
        await update.message.reply_text(text)
    else:
        await update.message.reply_text("No reminders found")
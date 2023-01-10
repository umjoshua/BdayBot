import sqlite3

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

async def start(update, context):
    await update.message.reply_text(startMessage)
    chatId = update.message.chat_id
    res = cursor.execute("SELECT * FROM users where userId  = ?",(chatId, ))
    if not res.fetchone():
       cursor.execute("INSERT INTO users VALUES (?)",(chatId,))
       print('no')

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
    await update.message.reply_text("I will remind you!")
    return 3
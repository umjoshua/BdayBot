startMessage = """
    Welcome!
    /new : create new reminder
    /view : view reminder
"""
new = "Whose birthday should I remember?"

name = None
date = None

async def start(update, context):
    await update.message.reply_text(startMessage)

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
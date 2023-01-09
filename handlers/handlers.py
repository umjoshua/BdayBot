startMessage = """
    Welcome!
    /new : create new reminder
    /view : view reminder
"""
new = "Whose birthday should I remember?"

async def start(update, context):
    await update.message.reply_text(startMessage)

async def newReminder(update, context):
    await update.message.reply_text(new)
    return 1

async def getName(update, context):
    await update.message.replay_text(new)
    # print('getName called')

async def getDate(update, context):
    await update.message.replay_text(new)

async def cancel(update,context):
    await update.message.replay_text("Cancelled!")
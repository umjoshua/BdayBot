from dotenv import load_dotenv
import os
from telegram.ext import *
from handlers import handlers
import datetime as dt

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

application.run_polling()
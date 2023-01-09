from dotenv import load_dotenv
import os
from telegram.ext import *
from handlers import handlers

load_dotenv()

application = Application.builder().token(os.getenv("TOKEN")).build()
application.add_handler(CommandHandler("start", handlers.start))

convHandler = application.add_handler(ConversationHandler(
    entry_points=[CommandHandler("new",handlers.newReminder)],
    states={
        1: [MessageHandler(filters.Text,handlers.getName)],
        2: [MessageHandler(filters.Text,handlers.getDate)],
    },
    fallbacks=[CommandHandler("cancel",handlers.cancel)],
))

application.run_polling()
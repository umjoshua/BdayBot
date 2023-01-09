from dotenv import load_dotenv
import os 
import telegram.ext

load_dotenv()

token = os.getenv("TOKEN")
bot = telegram.Bot(token=token)

startMessage = "Hello, Type /new to create new reminder!"

updater = telegram.ext.Updater(token,use_context=True)
dispatcher = updater.dispatcher
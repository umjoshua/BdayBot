# Telegram Birthday Bot
A telegram birthday reminder bot created in Python

## To Run
1. Set telegram bot TOKEN in .env
2. Run
```sh
pip3 install --no-cache-dir --requirement ./requirements.txt
cd database ; python3 dbscript.py
cd .. ; python3 main.py & ; python3 reminder.py &
```

## Alternatively, to run using docker,
```sh
docker build -t birthday-bot:1.0 .
```
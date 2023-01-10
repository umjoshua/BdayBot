FROM python:3.8.2-slim-buster
WORKDIR /app

COPY ./requirements.txt /app

RUN apt update
RUN apt install sqlite3 -y

RUN pip3 install --no-cache-dir --requirement ./requirements.txt

COPY . /app

RUN cd database ; python3 dbscript.py

RUN cd ..

CMD [ "python3","main.py","&",";","python3","reminder.py" ]
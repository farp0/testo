FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
#RUN pip3 install -U pip
RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . /app

#set a default command

CMD python3 bot.py

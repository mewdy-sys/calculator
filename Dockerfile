FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3-pip python3

RUN apt install -y python3-flask

COPY ./main.py /home/main.py

EXPOSE 5000

CMD bash & python3 /home/main.py

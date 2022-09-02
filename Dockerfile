FROM python:3.9.13-slim-buster

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

ENV LOG_PATH "/var/log/auth.log"

CMD python3 run.py

FROM python:3.7

ENV PYTHONUNBUFFERED 1

ADD . /code/personalblogapi

WORKDIR /code/personalblogapi

RUN pip install -r requirements.txt
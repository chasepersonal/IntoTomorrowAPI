FROM python:3

ENV PYTHONUNBUFFERED 1

ADD . /code/savepointapi

WORKDIR /code/savepointapi

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
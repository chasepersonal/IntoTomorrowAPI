FROM python:3.6-alpine

# Skip Buffereing
ENV PYTHONBUFFERED 1

# Skip .pyc files
ENV PYTHONDONTWRITEBYCODE 1

# To allow postgres config for Django Herkou
RUN apk add --no-cache --update build-base python3-dev py-pip jpeg-dev zlib-dev postgresql-dev gcc

# Make new app directory
RUN mkdir /app

# Set app directory as the working directory
WORKDIR /app

# Add the requirements.txt file to the app directory
ADD requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Add all files to the app directory
ADD . /app/
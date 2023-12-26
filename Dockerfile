FROM python:3.11

MAINTAINER Some Dev

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential gettext libpq-dev
#for mysql libmariadb-dev
# for pillow
RUN apt-get install -y libjpeg-dev zlib1g-dev libjpeg62-turbo-dev

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip uninstall cffi
RUN pip install cffi

COPY requirements.txt /tmp

RUN cd /tmp && pip install -r requirements.txt

RUN #adduser --disable-password service-user
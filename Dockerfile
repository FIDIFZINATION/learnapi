FROM python:3.7-alpine
MAINTAINER Fidifzi Nation ltd

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /learnapi
WORKDIR /learnapi
COPY ./learnapi /learnapi

RUN adduser -D fidifzi
USER fidifzi

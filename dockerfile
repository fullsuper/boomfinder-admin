FROM python:3.8.2-alpine3.11
LABEL maintainer="fullsuper"

ENV PYTHONUNBUFFED=1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user


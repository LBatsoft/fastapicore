FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apt-get update && apt-get install -y \
    python-dev python3-dev gcc libpq-dev \
    && pip3 install --upgrade setuptools

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /card_validator
WORKDIR /card_validator
COPY requirements.txt /card_validator/
RUN pip install -r requirements.txt
COPY . /card_validator/
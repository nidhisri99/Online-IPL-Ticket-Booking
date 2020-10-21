FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /ipl

WORKDIR /ipl

ADD requirements.txt /ipl/

RUN pip install — upgrade pip && pip install -r requirements.txt

ADD . /ipl/

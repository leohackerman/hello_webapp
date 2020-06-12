FROM python:3.7-slim

COPY src /srv/src
COPY requirements.txt /srv/src
WORKDIR /srv/src

RUN apt-get clean \
    && apt-get -y update

RUN pip install -r requirements.txt --src /usr/local/src
ENV PORT 8080
CMD python main.py
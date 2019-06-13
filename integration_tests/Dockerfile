FROM python:3.7-alpine
RUN apk update
RUN apk upgrade
RUN pip install quaerere-willamette-client
RUN mkdir /tmp/workdir
WORKDIR /tmp/workdir
COPY integration_runner.py /usr/bin/
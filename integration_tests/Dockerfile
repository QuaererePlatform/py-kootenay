FROM python:3.7-alpine
RUN apk update && apk upgrade
RUN mkdir /tmp/workdir
COPY requirements.txt /tmp/
COPY test_data.yaml /tmp/workdir/
COPY integration_runner.py /usr/bin/
RUN pip install -r /tmp/requirements.txt
WORKDIR /tmp/workdir
ENTRYPOINT ["integration_runner.py"]
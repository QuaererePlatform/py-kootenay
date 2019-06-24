FROM python:3.7-alpine
RUN apk update
RUN apk upgrade
RUN pip install PyYAML
RUN pip install python-arango
RUN pip install retrying
RUN mkdir /tmp/workdir
COPY test_data.yaml /tmp/workdir/
WORKDIR /tmp/workdir
COPY integration_runner.py /usr/bin/
ENTRYPOINT ["integration_runner.py"]
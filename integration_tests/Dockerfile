FROM python:3.7-alpine
RUN apk update && \
    apk upgrade && \
    mkdir /tmp/workdir /tmp/src
COPY * /tmp/src/
RUN pip install -r /tmp/src/requirements.txt && \
    cp /tmp/src/test_data.yaml /tmp/workdir/ && \
    cp /tmp/src/integration_runner.py /usr/bin/
WORKDIR /tmp/workdir
ENTRYPOINT ["integration_runner.py"]

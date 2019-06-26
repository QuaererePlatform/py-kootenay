FROM python:3.7-alpine
RUN apk update
RUN apk upgrade
RUN apk add gcc
RUN apk add git
RUN apk add musl-dev
RUN apk add yaml
RUN apk add yaml-dev
RUN mkdir /tmp/workdir
RUN mkdir /tmp/build
COPY willamette /tmp/build/willamette
COPY README.rst /tmp/build/
COPY LICENSE.txt /tmp/build/
COPY VERSION /tmp/build/
COPY setup.* /tmp/build/
WORKDIR /tmp/build/
RUN pip install "gunicorn[eventlet]>=19.9.0"
RUN python setup.py install
RUN apk del gcc
RUN apk del musl-dev
RUN apk del yaml-dev
COPY entrypoint.sh /usr/bin/
WORKDIR /tmp/workdir
ENTRYPOINT ["entrypoint.sh"]

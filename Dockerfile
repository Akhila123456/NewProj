# getting base image from Scratch
FROM python
MAINTAINER Akhila<akhila.i@happiestminds.com>
#ADD requirements.txt ./
COPY addition.py ./
#RUN python3 -m venv _venv && \
#    ./_venv/bin/pip3 install -qqr requirements.txt

RUN python addition.py


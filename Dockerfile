# getting base image from Scratch
FROM python
MAINTAINER Akhila<akhila.i@happiestminds.com>
COPY addition.py /
RUN python addition.py


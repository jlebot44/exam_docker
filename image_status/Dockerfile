FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y \
    python3 \
    pip \
    && pip install requests

ADD test_status.py /home/test_status.py

WORKDIR /home

CMD python3 test_status.py

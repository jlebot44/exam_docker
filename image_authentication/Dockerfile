FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y \
    python3 \
    pip \
    && pip install requests

ADD test_authentication.py /home/test_authentication.py

WORKDIR /home

ENTRYPOINT ["python3", "test_authentication.py"]

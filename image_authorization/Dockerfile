FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y \
    python3 \
    pip \
    && pip install requests

ADD test_authorization.py /home/test_authorization.py

WORKDIR /home

ENTRYPOINT ["python3", "test_authorization.py"]

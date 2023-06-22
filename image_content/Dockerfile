FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y \
    python3 \
    pip \
    && pip install requests

ADD test_content.py /home/test_content.py

WORKDIR /home

ENTRYPOINT ["python3", "test_content.py"]

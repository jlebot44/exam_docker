#!/bin/bash

docker volume create --name exam_docker
docker network create --subnet 172.20.0.0/16 --gateway 172.20.0.1 exam_docker_network


docker image build ./image_authentication -t test_authentication:latest
docker image build ./image_authorization -t test_authorization:latest
docker image build ./image_content -t test_content:latest





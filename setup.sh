#!/bin/bash

docker volume create --name exam_docker
docker network create --subnet 172.20.0.0/16 --gateway 172.20.0.1 exam_docker_network


docker image build ./image_authenticationt -t test_authentication:latest
docker image build ./image_authorization -t test_authorization:latest
docker image build ./image_content -t test_content:latest


docker container run -d -p 8000:8000 --network exam_docker_network --name api_to_test datascientest/fastapi:1.0.0


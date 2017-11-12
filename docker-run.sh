#!/usr/bin/env bash

docker rm sandeep/ml-service
docker rmi sandeep/ml-service

docker build -t sandeep/ml-service .

docker run  -p 5000:5000 sandeep/ml-service
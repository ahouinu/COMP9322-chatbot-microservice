#!/bin/sh

# run this script on local machine
docker build -t heroku-cli .
docker run -it --privileged heroku-cli
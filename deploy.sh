#!/bin/sh

# start docker daemon
dockerd&

# heroku auth
heroku container:login

# deploy timeslot service
cd /assn1/timeslots/timeslot-selection/ &&
sh deploy_timeslot.sh

# deploy dentist service
cd /assn1/dentist/dentist-selection/ &&
sh deploy_dentist.sh

# deploy dentist service
cd /assn1/chatbot &&
sh deploy_chatbot.sh
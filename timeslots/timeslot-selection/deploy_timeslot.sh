#!/bin/sh

# deploy timeslot service
heroku container:push web -a tim-9322-timeslot
heroku container:release web -a tim-9322-timeslot
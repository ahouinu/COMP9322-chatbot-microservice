#!/bin/sh

# deploy dentist service
heroku container:push web -a tim-9322-dentist
heroku container:release web -a tim-9322-dentist
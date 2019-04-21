FROM alpine:latest
# install dependencies
RUN apk add --update --no-cache curl bash nodejs docker
# install heroku-cli
RUN curl https://cli-assets.heroku.com/install.sh | sh
# set heroku api key
ENV HEROKU_API_KEY=''
RUN heroku update

# copy files into workspace
WORKDIR /assn1
COPY . /assn1

#CMD dockerd&
CMD sh deploy.sh
#ENTRYPOINT ["/bin/bash", "deploy_dentist.sh"]
#ENTRYPOINT ["/bin/bash", "deploy_timeslot.sh"]

FROM alpine:latest
RUN apk add --no-cache python3-dev
RUN pip3 install --upgrade pip
WORKDIR /service
COPY . /service
RUN pip3 install -r requirements.txt
ENV TIMESLOT_URL='http://tim-9322-timeslot.herokuapp.com'
ENV DENTIST_URL='http://tim-9322-dentist.herokuapp.com/'
CMD gunicorn app:app
#EXPOSE 5000
FROM alpine:latest
RUN apk add --no-cache python3-dev
RUN pip3 install --upgrade pip
WORKDIR /service
COPY . /service
RUN pip3 install -r requirements.txt
ENV MONGODB_URI='mongodb://heroku_2v117189:rlm5hpclss6mp9702vlf10jmhj@ds121495.mlab.com:21495/heroku_2v117189'
ENV MONGODB_DBNAME='heroku_2v117189'
CMD gunicorn "demo:create_app()"
#EXPOSE 5000
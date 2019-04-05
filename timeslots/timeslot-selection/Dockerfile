FROM alpine:latest
RUN apk add --no-cache python3-dev
RUN pip3 install --upgrade pip
WORKDIR /service
COPY . /service
RUN pip3 install -r requirements.txt
CMD gunicorn "demo:create_app()"
ENV MONGODB_URI='mongodb://heroku_s35sl8q3:ecfq6bh6fg6mie4oethvhq997g@ds019916.mlab.com:19916/heroku_s35sl8q3'
ENV MONGODB_DBNAME='heroku_s35sl8q3'
#EXPOSE 5000
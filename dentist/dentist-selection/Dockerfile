FROM alpine:latest
RUN apk add --no-cache python3-dev
RUN pip3 install --upgrade pip
WORKDIR /service
COPY . /service
RUN pip3 install -r requirements.txt
CMD gunicorn "demo:create_app()"
#EXPOSE 5000
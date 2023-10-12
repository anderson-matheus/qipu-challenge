from python:3.8-alpine
ADD . /app
COPY . /app
WORKDIR /app
CMD ['python']
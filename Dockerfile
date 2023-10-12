from python:3.8-alpine
ADD . /app
COPY . /app
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
WORKDIR /app
CMD ['python']
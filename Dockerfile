from python:3.8-alpine

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD . /app
COPY . /app

WORKDIR /app

ENTRYPOINT ["/bin/sh", "-c", "source /opt/venv/bin/activate && python3 -m http.server 5000"]
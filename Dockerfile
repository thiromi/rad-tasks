FROM python:3.10.4-slim

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

ENTRYPOINT ['python', '-m']

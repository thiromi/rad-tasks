ARG ENVIRONMENT="prod"
FROM python:3.10.4-slim as app-prod

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM app-prod AS app-dev
COPY requirements.dev.txt .
RUN pip install --no-cache-dir -r requirements.dev.txt

FROM app-${ENVIRONMENT} AS app

COPY . .
RUN pip install . --no-cache-dir

CMD python -m rad_task

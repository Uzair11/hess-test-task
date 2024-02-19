ARG PYTHON_VERSION=3.10.13
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV LANG C.UTF-8


ENV PYTHONUNBUFFERED=1

WORKDIR /app


ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser


RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

USER appuser

COPY . .

EXPOSE 8000

WORKDIR /app/testtask

CMD sh -c "cd /app/testtask && \
           echo 'Running migrations...' && \
           python manage.py migrate && \
           python manage.py ingestdata '/app/data.csv:csv,/app/data.json:json,/app/data.xml:xml' && \
           echo 'Starting Gunicorn...' && \
           gunicorn 'testtask.wsgi' --bind=0.0.0.0:8000"

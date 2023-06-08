# Stage 1: Build the application
FROM python:3.7-alpine AS builder

# Install build dependencies
RUN apk add --no-cache mariadb-dev build-base

WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app/

FROM builder as development

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
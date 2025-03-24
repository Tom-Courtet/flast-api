FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install gunicorn

ENV GUNICORN_CMD_ARGS="--workers=4 --bind=0.0.0.0:5000 --timeout 60 --access-logfile -"

EXPOSE 5000

CMD ["gunicorn", "flast-api:app"]
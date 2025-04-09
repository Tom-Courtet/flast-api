FROM python:3.9-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && pip install --no-cache-dir gunicorn

COPY . .

FROM gcr.io/distroless/python3

WORKDIR /app

# Copier tout le site-packages de Python où les modules sont installés
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
# Copier les fichiers de l'application
COPY --from=builder /app /app
# Copier les binaires Python
COPY --from=builder /usr/local/bin /usr/local/bin

ENV PYTHONPATH=/usr/local/lib/python3.9/site-packages
ENV GUNICORN_CMD_ARGS="--workers=4 --bind=0.0.0.0:5000 --timeout 60 --access-logfile -"

EXPOSE 5000

CMD ["/usr/local/bin/gunicorn", "flast-api:app"]
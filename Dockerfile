FROM python:3.11-slim

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements/base.txt .
RUN pip install --no-cache-dir -r base.txt

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . .

CMD ["/entrypoint.sh"]

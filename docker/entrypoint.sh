#!/bin/bash
set -e

# Wait for PostgreSQL
while ! nc -z db 5432; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

# Create migrations if needed
python manage.py makemigrations

# Run migrations
python manage.py migrate

# Create superuser if not exists
python manage.py shell -c "
from apps.users.models import User
if not User.objects.filter(phone='1234567890').exists():
    User.objects.create_superuser('1234567890', 'password')
"

# Start server
exec python manage.py runserver 0.0.0.0:8000

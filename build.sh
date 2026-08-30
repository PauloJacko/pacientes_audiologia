#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='Romina').exists() or \
User.objects.create_superuser('Romina', 'admin@saludaudiologica.cl', '4dm1n123.,')" \
| python manage.py shell
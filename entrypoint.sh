#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
python create_superuser.py

exec gunicorn kuop.wsgi:application --bind 0.0.0.0:8000

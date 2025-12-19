FROM python:3.12

WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "kuop.wsgi:application", "--bind", "0.0.0.0:8000"]
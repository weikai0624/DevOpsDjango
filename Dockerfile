FROM python:3.12

WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

RUN chmod +x /app/entrypoint.sh
EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]

CMD []
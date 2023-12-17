FROM python:3.11.1

ENV PYTHONUNBUFFERED 1

WORKDIR /app/backend

COPY requirements.txt /app/backend/

# Build psycopg2-binary from source -- add required required dependencies
RUN pip install -r requirements.txt

COPY . /app/backend/

EXPOSE 8000

#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
ENTRYPOINT ["/app/backend/django.sh"]
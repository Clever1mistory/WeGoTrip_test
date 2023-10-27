FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/shop

CMD python manage.py makemigrations && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 registration.wsgi:application
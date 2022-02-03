# Python Email Sender
This is an email sender that allows you to send out emails


## How to begin

### First - clone this project

```
git clone https://github.com/varfigstar/python_email_sender.git
```

### Install dependencies

````
pip install -r requirements.txt
````

### Apply migrations
````
python manage.py migrate
````

### Setup config
edit file 'email_sender/settings.py' with your values

````
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "example@gmail.com"
EMAIL_HOST_PASSWORD = "examplepassword"
EMAIL_USE_TLS = True

CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_TRACK_STARTED = True
````

### Run your broker
For redis:
````
redis-server
````

### Run server
````
python manage.py runserver
````

### Start celery worker
````
celery -A email_sender worker -l INFO
````
and for Windows:
````
celery -A email_sender worker -l INFO --pool=solo
````

# Mission completed!

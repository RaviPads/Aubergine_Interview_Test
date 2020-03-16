# Aubergine Test

This is for aubergine test only.

## Features

- [Python](https://www.python.org) 3.8
- [Django](https://www.djangoproject.com/) 3+
- Based on [Pipenv](https://github.com/kennethreitz/pipenv) - the officially recommended Python packaging tool from 
[Python.org](https://www.python.org).
- [Celery](http://www.celeryproject.org/) 4.4+
- [Rabbitm](https://www.rabbitmq.com/)
- Production settings to run Django-Server.
- HTTPS and other security related settings on Production.
- PostgreSQL database support with psycopg2.

## How to install & use pipenv
This project is intended to use [Pipenv](https://github.com/pypa/pipenv).
Use requirement.txt to install dependency.

```bash
cd project_dir
pip install pipenv
pipenv install
pipenv shell
pip install -r requirement.txt
```


## To start Django Project
Go to aubergine/aubergine directory.
Set proper parameter values according to production environment for django server.

```bash
SUPERUSER_EMAIL = "{{production superuser email}}"
SUPERUSER_PASSWORD = "{{production superuser password}}"
SECRET_KEY = "{{production Key}}"
ALLOWED_HOSTS = ["*"]
ADDITIONAL_APP = []  # Include environment specific apps
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
```

Set settings according for django database as well.

```bash
"NAME": "{{production database}}",
"USER": "{{production user}}",
"PASSWORD": "{{production password}}",
"HOST": "{{production host}}",
"PORT": "{{production port}}",
```
Set settings according to send email as well.

```bash
EMAIL_HOST = "{{Host Server}}"
EMAIL_USE_TLS = "True/False"
EMAIL_USE_SSL = "True/False"
EMAIL_PORT = "{{Host Port}}"
EMAIL_HOST_USER = "{{Host Email}}"
EMAIL_HOST_PASSWORD = "{{Host Password}}"
```

Choose appropriate django server environment then run command as stated here. 

```bash
cd aubergine
python manage.py migrate --noinput
python manage.py runserver
```

I have added some functionality here like hyperlink and you can check admin-panel also.

## For Task 1a
- User Registration
  - On Registration send an email to the User 
  - The email body should have verification link
After successful registration a verification link email will be sent to user's email address.
User can click on it and activate user's account on system.

```bash
-- To get user list and register user -- 
http://localhost:8000/users/  
```

## For Task 1b
- Setup Celery

```bash
---   aubergine/celery.py  ---
This file is to setup celery inside django and standalone.

---    registration/tasks.py  ---
This file contains all tasks which will be registered on celery

---    registration/run_task.py  ---
This file will call task and run it as celery task.
python -m aubergine.run_task

```
- Setup RabbitMQ

Anyone can use simple guide which is available on [official site](https://www.rabbitmq.com/install-windows.html) for install and setup rabbitmq server.

```bash
---   aubergine/celery.py  ---
This file we have used rabbitmq as broker.

app = Celery('aubergine', broker='amqp://localhost',backend='rpc', include=['registration.tasks'])

```

## For Task 1c
- After User Login (with credentials in Task 1a)
  - Add Multiple Image URLs
  - These Image URLs can be from any web storage like the S3 bucket.
  - On submitting of all these Image URLs store this URL's in the database in 2 ways:
    - Original URL of the Image
    - Compressed URL of the Image

Here django will ask email and password which is used into registration process.
On successful login user can see all images as well as add image urls.
image url is comma separated field. So user can add multiple urls.
On submit urls there will be two urls stored in database. Original and Compressed one.
which will be shown in image list.

 ```bash
 -- To add images -- 
http://localhost:8000/images/  

-- Compressed Image Path --
http://localhost:8000/image_path/<Image_ID>/

```


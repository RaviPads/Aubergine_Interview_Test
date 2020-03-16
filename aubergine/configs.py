SUPERUSER_EMAIL = "{{Production superuser email}}"
SUPERUSER_PASSWORD = "{{Production superuser password}}"

SECRET_KEY = "{{Production Key}}"

DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database for Production environment
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "{{Production database}}",
        "USER": "{{Production user}}",
        "PASSWORD": "{{Production password}}",
        "HOST": "{{Production host}}",
        "PORT": "{{Production port}}",
    }
}

# EMAIL_HOST and EMAIL_PORT settings. The EMAIL_HOST_USER and EMAIL_HOST_PASSWORD
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'email'
# EMAIL_HOST_PASSWORD = 'password'

EMAIL_HOST = "{{Host Server}}"
EMAIL_USE_TLS = "True/False"
EMAIL_USE_SSL = "True/False"
EMAIL_PORT = "{{Host Port}}"
EMAIL_HOST_USER = "{{Host Email}}"
EMAIL_HOST_PASSWORD = "{{Host Password}}"

try:
    from django.contrib.auth.models import User

    if not User.objects.filter(username=SUPERUSER_EMAIL).exists():
        User.objects.create_superuser(username=SUPERUSER_EMAIL, email=SUPERUSER_EMAIL, password=SUPERUSER_PASSWORD)
except Exception as e:
    print(e)
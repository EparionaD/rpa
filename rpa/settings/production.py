import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.rpa.pe','rpa.pe','143.244.179.7','localhost']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rpaDB',
        'USER': 'rpa',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

if DEBUG:
    STATICFILES_DIRS = [BASE_DIR, 'static']
else:
    STATIC_ROOT = os.path.join(BASE_DIR.parent, 'static')
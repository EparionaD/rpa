from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['167.99.119.117','localhost']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rpadb',
        'USER': 'rpa',
        'PASSWORD': 'ernesto123',
        'HOST': 'localhost',
        'PORT': '',
    }
}
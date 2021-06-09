import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

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

if DEBUG:
    STATICFILES_DIRS = [BASE_DIR, 'static']
else:
    STATIC_ROOT = os.path.join(BASE_DIR.parent, 'static')
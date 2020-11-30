from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['berdublog.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2jij3v6h874v',
        'USER': 'gbvuylqugaydxc',
        'PASSWORD': '3f5b1681c27f04e66fe641128bd14432c97c29686de9728bdbcf4e7572b0420d',
        'HOST': 'ec2-34-234-185-150.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
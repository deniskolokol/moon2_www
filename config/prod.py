from config.common import *

INSTALLED_APPS += ('storages',)
AWS_STORAGE_BUCKET_NAME = "moon2-static"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'moon2',
        'USER' : 'moon2root',
        'PASSWORD' : 'moon2',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

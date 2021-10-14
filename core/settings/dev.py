from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kingshousecr',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'PORT': '5432'
    }
}


CORS_ALLOW_ALL_ORIGINS = True

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

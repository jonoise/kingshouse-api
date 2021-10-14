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

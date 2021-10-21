import os
from .base import *
SECRET_KEY = 'django-insecure-#0-l8^$4=5&x2awr(%axx+8_6a0o(8(3o&95-+lj02%@5kr)rf'

DEBUG = True
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

import os
from .base import *
import django_on_heroku

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
CORS_ALLOWED_ORIGINS = ['https://www.kingshousecr.com']

django_on_heroku.settings(locals())

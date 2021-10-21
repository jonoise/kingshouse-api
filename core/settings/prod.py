import os
from .base import *
import django_on_heroku

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
CORS_ALLOWED_ORIGINS = ['https://www.kingshousecr.com']
ALLOWED_HOSTS = ['.herokuapp.com', 'kings-house-api.herokuapp.com']

django_on_heroku.settings(locals())

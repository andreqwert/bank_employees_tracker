import os
from environs import Env
import dj_database_url


env = Env()
env.read_env()

DJ_DATABASE_URL = env('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.parse(DJ_DATABASE_URL)
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'HOST': env('HOST'),
#         'PORT': env('PORT'),
#         'NAME': env('NAME'),
#         'USER': "guard",
#         'PASSWORD': env('PASSWORD'),
#     }
# }

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

ROOT_URLCONF = "project.urls"

DEBUG = env.bool("DEBUG")

INSTALLED_APPS = ['datacenter']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

from dotenv import load_dotenv
import os


load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv('ENGINE'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
        'NAME': os.getenv('NAME'),
        'USER': "guard",
        'PASSWORD': os.getenv('PASSWORD'),
    }
}

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = "project.urls"

DEBUG = bool(os.getenv("DEBUG").title())

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

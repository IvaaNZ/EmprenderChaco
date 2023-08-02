from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['Ivancito.pythonanywhere.com']



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#ESTA ES LA CONFIGURACION PARA BD SQLITE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Ivancito$default',
        'USER': 'Ivancito',
        'PASSWORD': '44266364414tita',
        'HOST': 'Ivancito.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
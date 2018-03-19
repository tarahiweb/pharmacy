"""
Django settings for pharmacy project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import user_profile
from os import environ
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get('PHARMA_SECRET', ')+9n8-f!_m$v7#a11&b=$s)t8o!t+1=z*vk&pk1_&*0n*nsric')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'PHARMA_PRODUCTION' not in environ

ALLOWED_HOSTS = ['*']
if not DEBUG:
    ALLOWED_HOStS = [] # ['127.0.0.1']


# Application definitiona

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Product',
    'user_profile',
    'pagedown',
    'cart',
    'orders',
    'refill',
    'emergency',
    'medicalspa',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pharmacy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processor.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'pharmacy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
if DEBUG:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       }
   }
else:
   DATABASES = {
       'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'emed',
            'USER': environ['PHARMA_DB_USER'],
            'PASSWORD': environ['PHARMA_DB_PASS'],
            'HOST': environ['PHARMA_DB_HOST'],
            'PORT': environ['PHARMA_DB_PORT'],
       }
   }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'user_profile.User'
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTHENTICATION_BACKENDS = ['user_profile.backends.EmailBackend']
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR,'email')



STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
CART_SESSION_ID = 'cart'

BRAINTREE_PRODUCTION = False
BRAINTREE_MERCHANT_ID = 'ggq27xkfrr5vdty2'
BRAINTREE_PUBLIC_KEY = 'kp447gtbr9b3cdpv'
BRAINTREE_PRIVATE_KEY = 'cde363753928cc4bb92a1ea764081257'





if not DEBUG:
    BRAINTREE_PRODUCTION = False
    BRAINTREE_MERCHANT_ID = environ['BRAINTREE_MERCHANT_ID']
    BRAINTREE_PUBLIC_KEY = environ['BRAINTREE_PUBLIC_KEY']
    BRAINTREE_PRIVATE_KEY = environ['BRAINTREE_PRIVATE_KEY']
    CELERY_BROKER_URL = environ['PHARMA_CELERY_BROKER_URL']

    STATIC_ROOT = '/home/emed/files/static'
    MEDIA_ROOT = '/home/emed/files/media'
    EMAIL_HOST = environ['PHARMA_EMAIL_HOST']

    EMAIL_HOST_USER = environ['PHARMA_EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = environ['PHARMA_EMAIL_HOST_PASSWORD']
    EMAIL_PORT = 465
    EMAIL_USE_TLS = True
    EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
    CELERY_EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
    DEFAULT_FROM_EMAIL = environ['PHARMA_EMAIL_HOST_FROM']
    INSTALLED_APPS += ["djcelery_email"]


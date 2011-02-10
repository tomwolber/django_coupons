# Django settings for django_coupons project.
import os
from conf.server_role import Role

''' 
Import server type. 
Choices are 'PROD', 'DEV', 'LOCAL' 
and are defined in conf/server_role.py:

class Role:
    def type(self):
        return "LOCAL"
'''
ROLE = Role()

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

if ROLE.type() == 'PROD': 
    
    DEBUG = False
    TEMPLATE_DEBUG = FALSE

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
    
    MEDIA_URL = 'http://127.0.0.1:8000/static/'    
    MEDIA_ROOT = os.path.join(SITE_ROOT, 'static')    

if ROLE.type() == 'DEV': 
    
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG 
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
    
    MEDIA_URL = 'http://127.0.0.1:8000/static/'    
    MEDIA_ROOT = os.path.join(SITE_ROOT, 'static')    

if ROLE.type() == 'LOCAL': # Settings for Local Use Only
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'dev1.db',                      
        }
    } 
    
    MEDIA_URL = 'http://127.0.0.1:8000/static/'    
    MEDIA_ROOT = os.path.join(SITE_ROOT, 'static')
    
    
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'sc^@ao@a)4l!-a!9(1n(!eprjp$vw^2p)+^n5gqz9l_!r7bg38'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'django_coupons.urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'apps.coupons',
    'apps.companies'
)
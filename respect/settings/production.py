from .includes.common import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "respect",
        "USER": "respect",
        "PASSWORD": DBPASSWORD,
        "HOST": "",
        "PORT": ""}}

SITE_TITLE = 'The 100% RESPECT! Campaign'
SITE_TAGLINE = ''

###################
# DEPLOY SETTINGS #
###################

GUNICORN_BIND = "127.0.0.1:8624"
PROCESS_USER = 'respect'
PROCESS_NAME = 'respect_production'
VIRTUALENV = 'production'

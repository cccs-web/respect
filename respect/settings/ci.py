from .includes.common import *

DEBUG = True

ALLOWED_HOSTS.append(u'respect_ci.crossculturalconsult.com')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "respect_ci",
        "USER": "respect",
        "PASSWORD": DBPASSWORD,
        "HOST": "",
        "PORT": ""}}

SITE_TITLE = 'The 100% Respect Campaign'
SITE_TAGLINE = None

###################
# DEPLOY SETTINGS #
###################

GUNICORN_BIND = "127.0.0.1:8625"
PROCESS_USER = 'respect'
PROCESS_NAME = 'respect_ci'
VIRTUALENV = 'ci'
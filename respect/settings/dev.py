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

VIRTUALENV = 'respect'

SITE_TITLE = 'The 100% Respect Campaign'
SITE_TAGLINE = None

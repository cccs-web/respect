#!/bin/bash
# Run the gunicorn service

# Make sure we're in the right virtual env and location
source /home/respect/.virtualenvs/production/bin/activate
source /home/respect/.virtualenvs/production/bin/postactivate

cd /home/respect/production

exec gunicorn -c /home/respect/production/_deploy/gunicorn.conf.py respect.wsgi:application
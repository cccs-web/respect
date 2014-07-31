#!/bin/bash
# Run the gunicorn service

# Make sure we're in the right virtual env and location
source /home/respect/.virtualenvs/ci/bin/activate
source /home/respect/.virtualenvs/ci/bin/postactivate

cd /home/respect/ci

exec gunicorn -c /home/respect/ci/deploy/gunicorn.conf.py respect.wsgi:application
#!/bin/bash
# Update the ci deployment

# Make sure we're in the right virtual env and location
source /home/respect/.virtualenvs/ci/bin/activate
source /home/respect/.virtualenvs/ci/bin/postactivate

cd /home/respect/ci
git pull
django-admin.py syncdb --noinput
django-admin.py collectstatic --noinput
sudo service respect_ci restart
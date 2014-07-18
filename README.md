These instructions are for Ubuntu 14.04 LTS. They should work on other Linux environments with minor tweaks.

## Set up the server environment

1. Install linux packages:

        ~ $ sudo apt-get install postgresql postgresql-contrib postgresql-server-dev-9.3 git python-dev python-setuptools
        ~ $ sudo apt-get install libjpeg-dev libpng-dev libfreetype6-dev

1. Fix image libraries

Ubuntu has these in an 'unusual' location for debian, so the following links ensure that things like Pillow find them.

        ~ $ sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
        ~ $ sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
        ~ $ sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

1. Install pip

NOTE: PIP is used to conveniently install Python modules needed for the project. If 'which pip' returns a path to pip, it is already installed. If it is not installed, follow these instructions:

get 'distribute_setup.py':

        ~ $ wget http://python-distribute.org/distribute_setup.py
        ~ $ sudo python distribute_setup.py

verify `easy install`:

        ~ $ which easy_install
        /usr/local/bin/easy_install

install `pip`:

        ~ $ sudo easy_install pip

verify `pip`:

        ~ $ which pip
        /usr/local/bin/pip


1. [Install virtualenwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)
Install `virtualenvwrapper` with `sudo`.

7. Create a new virtual environment and work within it

        ~ $ mkvirtualenv respect

You can name the virtualenv whatever you like, just be sure to adapt the remaining instructions appropriately.

NOTE If the `mkvirtualenv` returns a "command not found" error, follow these steps:

- check that 'virtualenvwrapper.sh' is in `/usr/local/bin`

- assuming that it is, use the `source` command to pass the contents of 'virtualenvwrapper.sh'to the Tcl interpreter:
    source /usr/local/bin/virtualenvwrapper.sh

- verify that this works by re-running the virtualenv command:

    mkvirtualenv respect

- exit virtualenv and `echo` the `source` command into the local user's `.bashrc`:

    deactivate
    echo 'source /usr/local/bin/virtualenvwrapper.sh' >> .bashrc

- verify contents of `.bashrc`

    tail .bashrc

1. Clone the repository and install the requirements

         (respect)~ $ git git@github.com:cccs-web/respect.git production
         (respect)~ $ cd production
         (respect)~/production $ pip install -r requirements.txt

This installs Django, Mezzanine and the other required Python modules.

1. Set up the virtual environment

These commands assume the settings and virtualenv - edit them as necessary.

         (respect)~/production $ add2virtualenv .
         (respect)~/production $ setvirtualenvproject
         (respect)~/production $ echo "export DJANGO_SETTINGS_MODULE=respect.settings.dev" >> ~/.virtualenvs/respect/bin/postactivate
         (respect)~/production $ deactivate
         ~/production $ workon respect
         ~/production $ activate
         (respect)~/production $

## Set up postgresql

Postgres can be fiddly to set up. Google is your friend.

1. Switch to postgres and add yourself as a super user:

        ~ $ sudo -iu postgres
        ~ $ psql -c 'CREATE USER <username> WITH SUPERUSER;'

1. Add the respect database and user.

         ~ $ psql -c "CREATE USER respect WITH PASSWORD 'password';"

This is most likely going to be achieved by using a dump of an existing database:

To make the database dump use pg_dump on an existing server with a valid respect database thus:

        ~ $ pg_dump -o -Fc respect >>> respect.pg_dump

Then restore it on the target system thus:

        ~ $ pg_restore -d postgres -C respect.pg_dump

Then ensure that the user has full access:

        ~ $ psql -c "GRANT ALL PRIVILEGES ON respect TO respect;"

If creating a database from scratch:

         (respect)~ $ psql -c "CREATE DATABASE respect WITH OWNER respect;"
         (respect)~ $ django createdb

The respect user must use md5 rather than peer access for postgres.
You may need to edit /etc/postgresql/9.3/main/pg_hba.conf and add a line for respect with md5 access specified.

### Dealing with locale issues

Postgres is very fussy about database locales. If the database you attempt to restore was created in a different locale,
you may find that it will fail with an "Invalid locale name: <locale_name>". If this happens, add the locale and restart
the postgres service:

    ~ $ sudo locale-gen en_AU.UTF-8
    Generating locales...
      en_AU.UTF-8... done
    Generation complete.
    ~ $ sudo service postgresql restart
     * Restarting PostgreSQL 9.3 database server     [ OK ]

## Install Nginx and upstart job

This is for public facing servers only.

         ~ $ sudo apt-get install nginx
         ~ $ sudo ln -s /home/respect/production/deploy/production_nginx /etc/nginx/sites-available/production
         ~ $ sudo ln -s /etc/nginx/sites-available/production /etc/nginx/sites-enabled/production
         ~ $ sudo service nginx restart
         ~ $ sudo cp /home/respect/production/deploy/production_upstart.conf /etc/init/respect_production.conf
         ~ $ sudo service respect_production start
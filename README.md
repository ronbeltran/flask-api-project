## To setup the project

    cd flask-api-project
    virtualenv venv
    touch venv/bin/postactivate
    touch venv/bin/workon_project

## Set the contents of venv/bin/workon_project (replace with your home directory prefix)

    #!/bin/sh
    source /home/rbeltran/Work/flask-api-project/venv/bin/activate
    source /home/rbeltran/Work/flask-api-project/venv/bin/postactivate

## Set the contents of venv/bin/postactivate

    DEBUG="true"
    SECRET_KEY="supersecret"


## To start developing

    source venv/bin/workon_project
    ./manage.py runserver


## Run the make file

    make lint # check the lint
    make test # run the tests


## Setup the Database

    $ sudo -i -u postgres
    [sudo] password for rbeltran:
    postgres@irosin:~$ psql
    psql (9.5.3)
    Type "help" for help.

    postgres=# CREATE DATABASE my_db;
    CREATE DATABASE
    postgres=# CREATE USER my_db_user WITH PASSWORD 'pass';
    CREATE ROLE
    postgres=# ALTER ROLE my_db SET client_encoding TO 'utf-8';
    ALTER ROLE
    postgres=# ALTER ROLE my_db SET default_transaction_isolation TO
    'read committed';
    ALTER ROLE
    postgres=# ALTER ROLE my_db SET timezone to 'UTC';
    ALTER ROLE
    postgres=# GRANT ALL PRIVILEGES ON DATABASE my_db to
    my_db_user;
    GRANT
    postgres=# ALTER USER my_db_user CREATEDB;
    ALTER ROLE
    postgres=# \du
                                             List of roles
          Role name       |                         Attributes                         | Member of
    ----------------------+------------------------------------------------------------+-----------
     my_db | Create DB                                                  | {}



## To obtain jwt token

    curl -X POST -d '{"username":"ronnie", "password":"pass"}' -H 'Content-Type: application/json' http://localhost:5000/auth

## To use the token

    curl -X GET http://localhost:5000/v1/api/accounts/hello -H "Authorization: Bearer {TOKEN}"

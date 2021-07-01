Usage
------
Locally with Docker

    $ docker-compose -f local.yml build

Locally no docker

    $ source env/bin/activate
    $ source runOnEditor // only one time
    $ python manage.py runserver  // run django
    $ source runOnEditorUnset // remove enviroment by runOnEditor
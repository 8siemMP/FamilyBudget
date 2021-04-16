# FamilyBudget
DjangoREST budget manager.

# Instalation and Running
To run project you need django compose installed on your system. To build and run project execute command `docker-compose up` in project main directory. After seeing communicate:

    Starting development server at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.

Open url: `localhost:8000` or `128.0.0.1:8000` in any web browser.


# Tests
To run unit tests execute command below after running dockers.

    $ docker-compose up
    $ docker-compose exec djangorest python manage.py tests

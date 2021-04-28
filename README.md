# FamilyBudget
DjangoREST budget manager.

# Instalation and Running
To run project you need django compose installed on your system. To build and run project execute command `docker-compose up` in project main directory. After seeing communicate:

    Starting development server at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.

You can browse now by browser or any http client like curl on urls: `localhost:8000`,  `128.0.0.1:8000` .

# Data
After running project database is empty. You can choose to:

## Start with clean database
You have to create your admin user by command: `docker-compose exec djangorest createsuperuser`. Later you can add more users by Admin Panel on url: `localhost:8000/admin`. Adding other data like budgets and Entries by admin panel is not recomended becouse of lack of data validation there.
API also gives ability to add users but without setting password.

## Load fixtures
There is prepared set of data in file fixtures.json. You can load them by command: `docker-compose exec djangorest ./manage.py loaddata fixtures.json`.
Admin user is: `alice` with password `admin1`, other users can be found in api list with passwords the same as usernames.

# Tests
To run unit tests execute command below after running dockers.

    $ docker-compose up
    $ docker-compose exec djangorest python manage.py tests

![Build](https://github.com/joshkotrous/devume-backend/actions/workflows/ci.yml/badge.svg)
![Code Quality](https://github.com/joshkotrous/devume-backend/actions/workflows/code_quality.yml/badge.svg)
[![codecov](https://codecov.io/gh/joshkotrous/devume-backend/graph/badge.svg?token=Y1D5M3L4OW)](https://codecov.io/gh/joshkotrous/devume-backend)
# Devumé
## Prerequisities
1. Python 3.10
2. PostgreSQL

## Database Setup
1. [Install PostgreSQL](https://www.postgresql.org/download/)
2. Start PostgreSQL
`brew services start postgresql`
3. Access the PostgreSQL CLI
`psql -U postgres`
4. Create the database
`CREATE DATABASE <database_name>;`

## Project Setup
1. [Install Python 3.10](https://www.python.org/downloads/release/python-31014/)
2. Clone the project
3. Open the project in a terminal and create a Python virtual environment
`python -m venv venv`
4. Activate your virtual environment
`source venv/bin/activate`
5. Install dependencies
`pip install -r requirements.txt`
6. Create your `.env` file
`cp .env.development .env`
7. Configure your `.env` variables
8. Create a super user
`python manage.py createsuperuser`
9. Migrate database models
`python manage.py makemigrations`
`python manage.py migrate`
10. Run the server
`python manage.py runserver`

## Where are things?
```.
├── app
└── devume
    ├── authentication
    ├── models
    ├── permissions
    ├── serializers
    ├── tests
    ├── utils
    └── views
```
- `app` - Contains `settings.py` and `urls.py`
- `devume/authentication` - custom authentication classes for API key authentication and bearer token authentication
- `devume/models` - database models
- `devume/permissions` - custom permission classes
- `devume/serializers` - data serializers for each models
- `devume/tests` - unit tests. Can be run with
`python manage.py test`. Tests are run upon opening a PR and coverage is reported to CodeCov
- `devume/utils` - utility functions. Contains general exception handler
- `devume/views` - all application views


## Authenticating Requests
Devumé supports Bearer Token authentication, session authentication, and API key authentication. For most requests, you will need to use API key authentication. In order to generate an API key:
1. Get the Bearer token for your super user with `POST http://localhost:8000/api/token` with your username and password in the JSON body:
```
{
    'username': <SuperUserUsername>,
    'password': <SuperUserPassword>
}
```
2. Create an API key using your bearer token for authentication with
`POST http://localhost:8000/api/key/create`

3. The API key can be used within the frontend `.env` for authentication or for testing requests

## Pre-commit hooks
Pre-commit is configured to run the Flake8 and Black to ensure code consistency.

## Contributing
Anyone is welcome to contribute to this repository. If you'd like to contribute, please review the open issues and open a corresponding PR for your change. Pre-commit hooks will be run upon opening your PR and will be required to pass before it can be merged.

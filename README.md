![Build](https://github.com/joshkotrous/devume-backend/actions/workflows/ci.yml/badge.svg)
![Code Quality](https://github.com/joshkotrous/devume-backend/actions/workflows/code_quality.yml/badge.svg)
# Devume
## Setup
### Prerequisities
1. Python 3.10
2. Docker

### Setup
1. Install Python 3.10
2. Install Docker
3. Clone the project
4. Open the project in a terminal and create a Python virtual environment `python -m venv venv`
5. Activate your virtual environment `source venv/bin/activate`
6. Install dependencies `pip install -r requirements.txt`
7. Create your `.env` file `cp .env.development .env`
8. Configure your `.env` variables
9. Run the server `python manage.py runserver`

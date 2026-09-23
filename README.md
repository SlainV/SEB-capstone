# NewsStream

A Django-based news publishing platform

## Features
- Custom user model
- Role-based access control
- Publishers and affiliations
- Article management
- Editorial review workflow
- Newsletter subscriptions
- REST API
- Administrator dashboard

## Roles
- Administrator
- Publisher Manager
- Journalist
- Editor
- Reader

# Manual installation from GitHub
## Installation prerequisites
python 3 with pip
git
MariaDB
- create a table in MariaDB with:
name = newsstream_db 
user = newsstream_user
password = strongpassword
-- username and password can be changed in config/settings.py

## Setup instructions
create a target folder and move into it (e.g. cd newsstream)

run:
git clone https://github.com/SlainV/NewsStream.git

move into newsstream folder
run:
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

- Create tables in the Database with:
python manage.py migrate

- Create default user groups in the Database with:
python manage.py create_groups

- Create a superuser with:
python manage.py createsuperuser

After creating the superuser:

1. Run the server: python manage.py runserver
2. Log into Django Admin. (http://localhost:8000/admin/)
3. Add the superuser to the Administrator group.
4. Thereafter manage users via the NewsStream Administrator Dashboard (http://localhost:8000/accounts/admin-dashboard/)

# Docker Setup Instructions
- Pull the docker container from the repository with:
docker pull slainv/newsstream

- Start the container with:
docker-compose up -d

- Create tables in the Database with:
docker compose exec web python manage.py migrate

- Create default user groups in the Database with:
docker compose exec web python manage.py create_groups

- Create a superuser with:
docker compose exec web python manage.py createsuperuser

After creating the superuser:

1. Run the server: python manage.py runserver
2. Log into Django Admin. (http://localhost:8000/admin/)
3. Add the superuser to the Administrator group.
4. Thereafter manage users via the NewsStream Administrator Dashboard (http://localhost:8000/accounts/admin-dashboard/)
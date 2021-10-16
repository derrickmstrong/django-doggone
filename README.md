# Django

### Create Project
django-admin startproject PROJECTNAME

### Setup .env variable(s)
Follow instructions: https://djangocentral.com/environment-variables-in-django/

https://django-environ.readthedocs.io/en/latest/

### Add .gitignore file
Include the following:
.env
.env.example
*.cpython-39.pyc

### Run Project
python3 manage.py runserver
localhost:8000

### Run migrate to fix any errors
python3 manage.py migrate
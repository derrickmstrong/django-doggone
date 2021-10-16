# Doggone - a Django project

## This app is a detective agency that finds dogs. There are Lost dogs and Found dogs and we try to get them back home to their parents.

### Create Project
django-admin startproject PROJECTNAME

### Setup .env variable(s)
Follow instructions: 
https://djangocentral.com/environment-variables-in-django/

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

### Create app
python3 manage.py startapp APPNAME

### Add new app to settings.py under INSTALLED_APPS
'appname'

### Create models


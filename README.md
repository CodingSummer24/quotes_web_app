# Quotes - Django sample applications

## How to run:
1. Clone the project
1. cd in the quotes_web_app directory
1. Create a virtual environment: `python -m venv venv`
1. Activate the virtual environment: `venv\Scripts\Activate` (MS-Windows), `source venv/bin/activate` (Linux/Mac)
1. Install libraries: `pip install -r requirements.txt`
1. Create the Django project: `django-admin startproject quotes`
1. cd into the quotes folder
1. Create the database: `python manage.py migrate`
1. Create admin user: `python manage.py createsuperuser`
1. Run the app: `python manage.py runserver`
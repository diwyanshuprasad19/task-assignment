## Task Management System (Django Rest Framework)

This is a simple Task Management System built using Django and Django REST Framework. The application provides APIs for creating tasks, assigning tasks to users, and fetching user-specific tasks.

---

## 📌 Installation

## 1. Clone the Repository

git clone git@github.com:diwyanshuprasad19/task-assignment.git


## Set Up Virtual Environment
Create a virtual environment to isolate dependencies.

python3 -m venv myenv


## Activate the virtual environment:

On Windows:

myenv\Scripts\activate


On macOS/Linux:

source myenv/bin/activate


## Requirements

pip install -r requirements.txt

## 4. Apply Migrations
Generate and apply migrations for the application.

python manage.py makemigrations accounts task

python manage.py migrate

## Run the Server
Start the Django development server.

python manage.py runserver

The application will be running at:

http://127.0.0.1:8000/

## Admin credentials

Email: admin@local.com

Password: 12345

## API Testing
You can test the APIs using two ways:

1. api_test.txt

This file contains sample request-response pairs for all available APIs.

2. api_collection.json (Postman Collection)

Import this file into Postman to quickly access and test all the APIs.

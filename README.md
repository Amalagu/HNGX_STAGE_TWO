# HNGX_STAGE_TWO

-A simple REST API capable of CRUD operations on a "person" resource, interfacing with any database of your choice. Your API should dynamically handle parameters, such as adding or retrieving a person by name

# Tech Stack

-coreapi==2.3.3
-Django==4.2.5
-djangorestframework==3.14.0
-PyYAML==6.0.1
-uritemplate==4.1.1

# Installation

-Clone the repo

-Run `pip install -r requirements.txt` in your terminal to install packages in the requirements.txt file

-Finally run `python manage.py runserver` in your terminal to start the app

#Endpoints

-user: [ POST: create a new user] /api/
[ GET: get a single user] /api/<id>
[ PUT: update or replace auth] /api/<id>
[ DELETE: delete a user] /api/<id>

docs: [ GET: get API Documentation] /api/docs

Database Schema :

API Documentation : /api/docs

API Live Link :

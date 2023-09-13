# HNGX_STAGE_TWO

-A simple REST API capable of CRUD operations on a "person" resource, interfacing with a Sqlite database. This API dynamically handle parameters, such as adding or retrieving a person by name or by id

# Tech Stack

- coreapi==2.3.3
- Django==4.2.5
- djangorestframework==3.14.0
- PyYAML==6.0.1
- uritemplate==4.1.1

# Installation

- Clone the repo: `git clone https://github.com/Amalagu/HNGX_STAGE_TWO.git`

- Navigate to the project: `cd HNGX_STAGE_TWO`

- Install the required packages: `pip install -r requirements.txt`

- Start the app: `python manage.py runserver`

# Endpoints

### user:

[ POST: create a new user] `/api/`

[ GET: get a single user] `/api/<id>`

[ GET: get a user (or users) by fullname] `/api?fullname=<fullname>`

[ PUT: update or replace auth] `/api/<id>`

[ DELETE: delete a user] `/api/<id>`

### docs:

[ GET: get API Documentation] `/api/docs`

#

Database UML Schema Diagram: `https://dbdiagram.io/d/6501a1bb02bd1c4a5e7e11f9`

Database Schema : `/api/schema`

API Documentation : `/api/docs`

API Live Link :

#

Tests are contained in the `test.py` file.
To run the tests, type:

- `cd hngcrud`
- `python manage.py test`

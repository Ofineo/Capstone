# FSND Capstone API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7.2

Follow instructions to install the version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

It's good practise to work within a virtual environment whenever using Python. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

```
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we use to handle cross origin requests from the frontend server. 

## Database Setup

Create a new database in Postgress:
```
createdb Capstone
```

With Postgres running, restore the database
```
psql Capstone < Capstone_bak.sql
```
## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:
```
source env_bash.sh
```

## Testing
To run the tests, run:
```
dropdb Capstone_test && createdb Capstone_test
psql Capstone_test < Capstone_bak.sql
python test_Capstone.py
```

# API Endpoints

> Base URL `Localhost:5000`

URI|Method|Action|Curl example|return example
---|---|---|---|---
/|GET|test the application is running|`curl localhost:5000/`|'Hi There'
/actors|GET|Fetches all the actors as a List|`curl localhost:5000/actors -H"Authorization: Bearer <Token>"`|`{"actors": [{"age": 54, "gender": "male", "id": 7, "name": "Otilio"}, {"age": 45, "gender": "male", "id": 9, "name": "pepe Gotera"},], "status": true}`|
/Movies|GET|Fetches all the movies as a List|`curl localhost:5000/movies -H"Authorization: Bearer <Token>"`|`{"movies": [{      "actor_id": 4, "id": 13, "release date": "Sun, 17 May 2020 00:00:00 GMT", "title": "random title" }, {"actor_id": 1, "id": 8, "release date": "Thu, 25 Mar 2021 11:55:11 GMT", "title": avengers vs godzilla" }],"status": true }`|
/actors/<id>|PATCH|Modifies the content of a stored actor. Returns the modified actor as a list|`curl localhost:5000/actors/2 -X PATCH -H"Authorization: Bearer <Token>" -H"Content-Type: application/json" -d'{"name":"Otilio", "age":"54"}'`|`{"actor": [{"age": 54, "gender": "male", "id": 2, "name": "Otilio"}], status": true}`|
/movies/<id>|PATCH|Modifies the content of a stored movie. Returns the modified actor as a list|`curl localhost:5000/movies/5 -X PATCH -H"Authorization: Bearer <Token>" -H"Content-Type: application/json" -d'{"title":"avengers vs godzilla","releaseDate":"2021-03-25 11:55:11.271041"}'`|`{"movie": [{"actor_id": 1, "id": 5, "release date": "Thu, 25 Mar 2021 11:55:11 GMT", "title": "avengers vs godzilla"}], "status": true}`|
/actors/<id>|DELETE|Deletes the selected actor by specified id|`curl localhost:5000/actors/3 -X DELETE -H"Authorization: Bearer <Token>"`|`{"actor": "3", "status": true}`|
/movies/<id>|DELETE|Deletes the selected movie or movies with title specified by id|`curl localhost:5000/movies/1 -X DELETE -H"Authorization: Bearer <Token>"`|`{"movie": "por amor", "status": true}`|
/actors/add|POST|Adds a new actor to the database. Returns the actor as a List|`curl localhost:5000/actors/add -X POST -H"Authorization: Bearer <Token>" -H"Content-Type: application/json" -d'{"name":"pepe Gotera", "age":"45","gender":"male"}'`|`{ "actor": [{"age": 45, "gender": "male", "id": 1, "name": "pepe Gotera" }], "status": true }`|
/movies/add|POST|Adds a new movie to the database. Returns the movie as a List. If more than one actor is specified on the actors List one identical movie will be created for each actor.|`curl -X POST localhost:5000/movies/add  -H"Authorization: Bearer <Token>" -H"Content-Type: application/json" -d'{"title":"random title","releaseDate":"2020-03-25 11:55:11.271041","actor_id": ["1","2","4"]}'`|`{ "movie": [{"actor_id": "1", "id": null, "release date": "Sun, 17 May 2020 00:00:00 GMT", "title": "random title" }, { "actor_id": "2", "id": null, "release date": "Sun, 17 May 2020 00:00:00 GMT", "title": "random title" },{"actor_id": "4", "id": null, "release date": "Sun, 17 May 2020 00:00:00 GMT", "title": random title"}], "status": true}`|


## Test tokens:

#### Casting assistant

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9USXpNakl6UkVZMFJEQXdNRGN3UTBFNVF6TTBNekE0TURNMVF6bERRVGRFUVRNeE1VUXpNdyJ9.eyJpc3MiOiJodHRwczovL29maW5lby5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU3YjkyNDNjMWFkNWEwYzViNWE5MDQ3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1ODUyMTE0NzksImV4cCI6MTU4NTI5Nzg3OSwiYXpwIjoiMzVNNTJYbEgxM1R6NDl6T3gzQXBkUTdrNmY3Y1Fnb2wiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.eZvHGtOwlBSgASFFYKfMLxdLc2zUrxrLRG1z-oPzwSaqfYBbOyuJkTpfWrr5YjTuG3WovtwjzmLBhFyNJIs4LickEwAUcSe4iU6htGylV1YZlg7qmbt-4OU9z9KJOwRht1LC8gKAXfmqWKlTXAzyoTHizMPtSCyJcfhjz8HvRxBzDxS9o9ZUzWoRzBudxYJ5-6MfGiqZrTzNtZn2q9XghnIIPHVeJvG-WGr9LlkV72GrGtrazik2yT6BnrCccSFlp8fMBf9i76oZ56wRT-DzX11rtEaL9k7VL4biMmgJeVwHUibAp10Aa8IzNJIC7w2rulnKbWzow_C8vxBYJYtowg`

#### Casting director

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9USXpNakl6UkVZMFJEQXdNRGN3UTBFNVF6TTBNekE0TURNMVF6bERRVGRFUVRNeE1VUXpNdyJ9.eyJpc3MiOiJodHRwczovL29maW5lby5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU3YjkyN2VmNjE3NGUwYzY1ZTAyOTE5IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1ODUxNTk1NzQsImV4cCI6MTU4NTI0NTk3NCwiYXpwIjoiMzVNNTJYbEgxM1R6NDl6T3gzQXBkUTdrNmY3Y1Fnb2wiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.LZpCG3DD_i7XgFHI1cCj7vvdTjrbKKECPGbAGlvpeG6kkmepCajBNBqoF5A0bkIBNk5bidS_VSq-aybrsvGoDrtmMpeZloJLEZ8A3A4ag3OZTGbrx_iwdFdu-u2L_UaaL2tqntZh4glhE88DZ_nETnrmVFukPMsMpHicecgHgRBWS5eH2D8Em_O-HvrOt5xX2B9feVgIv_oLIKL6Osf4ghmshmJJwxWY0Mc9wmHnv9kwNQ_mPu9cFuZb-nlBeaDBcry5SiK_pqiiZsJW2UxMA6bo8cPBh2J-h0nSLXzEZ0tNyNSx3HEl4hFoULRTcRCthRc5mcHzwKZEDkXwwiNLGQ`

#### Executive producer

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9USXpNakl6UkVZMFJEQXdNRGN3UTBFNVF6TTBNekE0TURNMVF6bERRVGRFUVRNeE1VUXpNdyJ9.eyJpc3MiOiJodHRwczovL29maW5lby5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU3YzY4Y2ExMWRkNDkwYzZiM2VlNTM0IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1ODUzMDAyMjUsImV4cCI6MTU4NTM4NjYyNSwiYXpwIjoiMzVNNTJYbEgxM1R6NDl6T3gzQXBkUTdrNmY3Y1Fnb2wiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.WSJMNDMlOy7bkcJMePO1RKKSHpfcxdbcC_GCOepLKYgBRRfuuDUt76555m1ZD2V0FYlcicpquA0uqqvOXyt-4aepqbUvauI02zt-7aALae8cbYlqvulcSrPTzfON_wJu3YSdLjYtHbvoLg7zL-umTTI4Fozb63UPbQGb_rQD9IwU_ud8s7wb1mCSqpZzczNbI7FrYp2F-I5T1gEY3zvAOtygasC5d-jQ8t3mYRq4GJcROQ83bolkrI0fX4ynIxqow2vh89zBb6E8KZt1vly0IuocViK_4XRGr5fhLc4vgusjhdua-R4Pr6zjP4sTX4Mq-b16JfKGFvoUNh9DwpUOtw`


## Permissions

Permissions|Details
---|---
get:movies|Gets access to all movies
get:actors|Gets access to all actors
post:actors|Can add actors to the DB
post:movies|Can add movies to the DB
delete:actors|Can delete actors from the DB
delete:movies|Can delete movies from the DB
patch:actors|Can modify actors from the DB
patch:movies|Can modify movies from the DB

## Roles
ofineo@gmail.com
C@stn302193
ofineo@hotmail.com
basura@outlook.jp

Role|Permissions
---|---
Casting Assistant| get:movies get:actors
Casting Director| get:movies get:actors post:actors delete:actors  patch:actors patch:movies
Executive producer| get:movies get:actors post:actors post:movies delete:actors delete:movies patch:actors patch:movies

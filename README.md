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
## Running the server locally

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

## Live server can be found in

> Base URL `https://capstone-fsnd-2020.herokuapp.com/`


# API Endpoints

> Base URL `https://capstone-fsnd-2020.herokuapp.com/`

URI|Method|Action|Curl example|return example
---|---|---|---|---
/|GET|test the application is running|`curl https://capstone-fsnd-2020.herokuapp.com/`|'Hi There'
/actors|GET|Fetches all the actors as a List|`curl https://capstone-fsnd-2020.herokuapp.com//actors -H"Authorization: Bearer <Token>"`|`{"actors": [{"age": 54, "gender": "male", "id": 7, "name": "Otilio"}, {"age": 45, "gender": "male", "id": 9, "name": "pepe Gotera"},], "status": true}`|
/Movies|GET|Fetches all the movies as a List|`curl https://capstone-fsnd-2020.herokuapp.com//movies -H"Authorization: Bearer <Token>"`|`{"movies": [{      "actor_id": 4, "id": 13, "release date": "Wed, 25 Dec 2020 22:55:56 GMT", "title": "random title" }, {"actor_id": 1, "id": 8, "release date": "Thu, 25 Mar 2021 11:55:11 GMT", "title": avengers vs godzilla" }],"status": true }`|
/actors/<id>|PATCH|Modifies the content of a stored actor. Returns the modified actor as a list|`curl https://capstone-fsnd-2020.herokuapp.com//actors/2 -X PATCH -H"Authorization: Bearer <Token>" -H"Content-Type: application/json" -d'{"name":"Otilio", "age":"54"}'`|`{"actor": [{"age": 54, "gender": "male", "id": 2, "name": "Otilio"}], status": true}`|
/movies/<id>|PATCH|Modifies the content of a stored movie. Returns the modified actor as a list|`curl https://capstone-fsnd-2020.herokuapp.com//movies/5 -X PATCH -H"Authorization: Bearer <Token>" -H"Content-Type: application/json" -d'{"title":"avengers vs godzilla","releaseDate":"Wed, 25 Dec 2020 22:55:56 GMT"}'`|`{"movie": [{"actor_id": 1, "id": 5, "release date": "Thu, 25 Mar 2021 11:55:11 GMT", "title": "avengers vs godzilla"}], "status": true}`|
/actors/<id>|DELETE|Deletes the selected actor by specified id|`curl https://capstone-fsnd-2020.herokuapp.com//actors/3 -X DELETE -H"Authorization: Bearer <Token>"`|`{"actor": "3", "status": true}`|
/movies/<id>|DELETE|Deletes the selected movie or movies with title specified by id|`curl https://capstone-fsnd-2020.herokuapp.com//movies/1 -X DELETE -H"Authorization: Bearer <Token>"`|`{"movie": "por amor", "status": true}`|
/actors/add|POST|Adds a new actor to the database. Returns the actor as a List|`curl https://capstone-fsnd-2020.herokuapp.com//actors/add -X POST -H"Authorization: Bearer <Token>" -H"Content-Type: application/json" -d'{"name":"pepe Gotera", "age":"45","gender":"male"}'`|`{ "actor": [{"age": 45, "gender": "male", "id": 1, "name": "pepe Gotera" }], "status": true }`|
/movies/add|POST|Adds a new movie to the database. Returns the movie as a List. If more than one actor is specified on the actors List one identical movie will be created for each actor.|`curl -X POST https://capstone-fsnd-2020.herokuapp.com//movies/add  -H"Authorization: Bearer <Token>" -H"Content-Type: application/json" -d'{"title":"random title","releaseDate":"Wed, 25 Dec 2020 22:55:56 GMT","actor_id": ["1","2","4"]}'`|`{ "movie": [{"actor_id": "1", "id": null, "release date": "Wed, 25 Dec 2020 22:55:56 GMT", "title": "random title" }, { "actor_id": "2", "id": null, "release date": "Wed, 25 Dec 2020 22:55:56 GMT", "title": "random title" },{"actor_id": "4", "id": null, "release date": "Wed, 25 Dec 2020 22:55:56 GMT", "title": random title"}], "status": true}`|


## Test tokens:

#### Casting assistant

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9USXpNakl6UkVZMFJEQXdNRGN3UTBFNVF6TTBNekE0TURNMVF6bERRVGRFUVRNeE1VUXpNdyJ9.eyJpc3MiOiJodHRwczovL29maW5lby5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU3YjkyNDNjMWFkNWEwYzViNWE5MDQ3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1ODUzMDY2NjYsImV4cCI6MTU4NTM5MzA2NiwiYXpwIjoiMzVNNTJYbEgxM1R6NDl6T3gzQXBkUTdrNmY3Y1Fnb2wiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.K5GtI9nTZQdMkDxnhwoHSWT0DumfuSILEMf1FnaRMfVHnxzXfy2FSthuAZVu0IZ9NCYF1JxWM4GFpogwUUSGowicMeI0ZR9GoaH1Z0BgTp1z4H-lroKoQDsddB0ihs0b4j67U58NwkWfGTvIBCXf9CHasfwI7MpbGz3ZF4RAfPKn6WP2CwhxkWDQlZq611aWEIrR4i7Pi5GBht3tJBlQqbzthZyBAvEe6AdoILgu3BekT_nN1o8-FPO2CadJI0-CwxeD6ruNfRiDE4IAN7rhenPW2RTIpHkfP7MQ31DkFZdWQZJcrrHabpo2Wjt3d7n5ja1XBEH4lp0JmWGYvDO3YA`

#### Casting director

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9USXpNakl6UkVZMFJEQXdNRGN3UTBFNVF6TTBNekE0TURNMVF6bERRVGRFUVRNeE1VUXpNdyJ9.eyJpc3MiOiJodHRwczovL29maW5lby5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU3YjkyN2VmNjE3NGUwYzY1ZTAyOTE5IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1ODUzMDY2MTQsImV4cCI6MTU4NTM5MzAxNCwiYXpwIjoiMzVNNTJYbEgxM1R6NDl6T3gzQXBkUTdrNmY3Y1Fnb2wiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.mPTLtrcy3jy9IoHBBI4ZgWKojvm7j-k421JNshVF_NF6WXo-hmtX9AptlzCQFfgq53qMnEYUc7_fHPPKhFIW3TKc6zB4qP9anhPIyAy_tdoc932CDRkdXFacT6oM8Rpma5-NRFvQ9X4QaKEYNq9GHFuzBhc18t0euSpGGIogX19wab6twuEAL1N7XiALU40CWcpuvxAsEkfig6HUsrNtHWcmrByCg-OszGqgyzhBXovxbd0pRcmd0WLuSkg_iLNz5rVlLrlH_gXZ62DLyuamldud4Th32rqwpsEAQJPN9YnmY-YZImy0x0V0NRN5g5rMvWN6TH1m-NYorzEMfERdYg`

#### Executive producer

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9USXpNakl6UkVZMFJEQXdNRGN3UTBFNVF6TTBNekE0TURNMVF6bERRVGRFUVRNeE1VUXpNdyJ9.eyJpc3MiOiJodHRwczovL29maW5lby5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU3YzY4Y2ExMWRkNDkwYzZiM2VlNTM0IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1ODU0MTA0OTQsImV4cCI6MTU4NTQ5Njg5NCwiYXpwIjoiMzVNNTJYbEgxM1R6NDl6T3gzQXBkUTdrNmY3Y1Fnb2wiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.llU-ywRaHC4N0Nt0RF4tshLaAndC87HeROIEeetho1EJ8F3B0xLivmFwLPgRiJHNkBaWVJSVdbdk3ZOfNP5imSMStfvKOWriNyL0gqUctEtqUjba0fhbTSlsa4EBaIy1BGnBStFJLlj1OIdtcazChzyi5vmf4IrcgiI6kzkgpIy-HVgYC8BO2koG7UnkObYnjP3m484Ic1eVmPXWJ0zA-gldrzP7xMxyh7swdVKnJP0c_c7B8xTz2KfGyrX6AjjPz6FhoTmV241_FwmwqHYPCKU0L1XV7qOypv86wbmXDgQJGvO5VNSoz41twsXLBpiq2Zz60RBXafoS91XRFiF5qQ`


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

Role|Permissions
---|---
Casting Assistant| get:movies get:actors
Casting Director| get:movies get:actors post:actors delete:actors  patch:actors patch:movies
Executive producer| get:movies get:actors post:actors post:movies delete:actors delete:movies patch:actors patch:movies

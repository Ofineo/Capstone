


#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.


pip freeze > requirements.txt

pycodestyle .

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
/movies/<id>|DELETE|Deletes the selected movie by specified id|`curl localhost:5000/movies/3 -X DELETE -H"Authorization: Bearer <Token>"`|`{"movie": "3", "status": true}`|
/actors/add|POST|Adds a new actor to the database. Returns the actor as a List|`curl localhost:5000/actors/add -X POST -H"Authorization: Bearer <Token>" -H"Content-Type: application/json" -d'{"name":"pepe Gotera", "age":"45","gender":"male"}'`|`{ "actor": [{"age": 45, "gender": "male", "id": 1, "name": "pepe Gotera" }], "status": true }`|
/movies/add|POST|Adds a new movie to the database. Returns the movie as a List. If more than one actor is specified on the actors List one identical movie will be created for each actor.|`curl -X POST localhost:5000/movies/add  -H"Authorization: Bearer <Token>" -H"Content-Type: application/json" -d'{"title":"random title","releaseDate":"2020-03-25 11:55:11.271041","actor_id": ["1","2","4"]}'`|`{ "movie": [{"actor_id": "1", "id": null, "release date": "Sun, 17 May 2020 00:00:00 GMT", "title": "random title" }, { "actor_id": "2", "id": null, "release date": "Sun, 17 May 2020 00:00:00 GMT", "title": "random title" },{"actor_id": "4", "id": null, "release date": "Sun, 17 May 2020 00:00:00 GMT", "title": random title"}], "status": true}`|


## Test tokens:

#### Casting assitant

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9USXpNakl6UkVZMFJEQXdNRGN3UTBFNVF6TTBNekE0TURNMVF6bERRVGRFUVRNeE1VUXpNdyJ9.eyJpc3MiOiJodHRwczovL29maW5lby5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU3YjkyNDNjMWFkNWEwYzViNWE5MDQ3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1ODUyMTE0NzksImV4cCI6MTU4NTI5Nzg3OSwiYXpwIjoiMzVNNTJYbEgxM1R6NDl6T3gzQXBkUTdrNmY3Y1Fnb2wiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.eZvHGtOwlBSgASFFYKfMLxdLc2zUrxrLRG1z-oPzwSaqfYBbOyuJkTpfWrr5YjTuG3WovtwjzmLBhFyNJIs4LickEwAUcSe4iU6htGylV1YZlg7qmbt-4OU9z9KJOwRht1LC8gKAXfmqWKlTXAzyoTHizMPtSCyJcfhjz8HvRxBzDxS9o9ZUzWoRzBudxYJ5-6MfGiqZrTzNtZn2q9XghnIIPHVeJvG-WGr9LlkV72GrGtrazik2yT6BnrCccSFlp8fMBf9i76oZ56wRT-DzX11rtEaL9k7VL4biMmgJeVwHUibAp10Aa8IzNJIC7w2rulnKbWzow_C8vxBYJYtowg`

#### Casting director

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9USXpNakl6UkVZMFJEQXdNRGN3UTBFNVF6TTBNekE0TURNMVF6bERRVGRFUVRNeE1VUXpNdyJ9.eyJpc3MiOiJodHRwczovL29maW5lby5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU3YjkyN2VmNjE3NGUwYzY1ZTAyOTE5IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1ODUxNTk1NzQsImV4cCI6MTU4NTI0NTk3NCwiYXpwIjoiMzVNNTJYbEgxM1R6NDl6T3gzQXBkUTdrNmY3Y1Fnb2wiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.LZpCG3DD_i7XgFHI1cCj7vvdTjrbKKECPGbAGlvpeG6kkmepCajBNBqoF5A0bkIBNk5bidS_VSq-aybrsvGoDrtmMpeZloJLEZ8A3A4ag3OZTGbrx_iwdFdu-u2L_UaaL2tqntZh4glhE88DZ_nETnrmVFukPMsMpHicecgHgRBWS5eH2D8Em_O-HvrOt5xX2B9feVgIv_oLIKL6Osf4ghmshmJJwxWY0Mc9wmHnv9kwNQ_mPu9cFuZb-nlBeaDBcry5SiK_pqiiZsJW2UxMA6bo8cPBh2J-h0nSLXzEZ0tNyNSx3HEl4hFoULRTcRCthRc5mcHzwKZEDkXwwiNLGQ`

#### Executive producer

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9USXpNakl6UkVZMFJEQXdNRGN3UTBFNVF6TTBNekE0TURNMVF6bERRVGRFUVRNeE1VUXpNdyJ9.eyJpc3MiOiJodHRwczovL29maW5lby5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU3YzY4Y2ExMWRkNDkwYzZiM2VlNTM0IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1ODUyMTE3ODksImV4cCI6MTU4NTI5ODE4OSwiYXpwIjoiMzVNNTJYbEgxM1R6NDl6T3gzQXBkUTdrNmY3Y1Fnb2wiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.s2ZdhS_O7cTCaD92vHdz_nnCI02VG4w4lWy_C5IOi7Ubx5O4HLEJUFKlqSXLOfAGnZrk1bwvhtC2uFcMT6dG8PFvS4zaWeMKVMQM0mFKKnAoEX_y9vXXyBAtj3tl7NqUqyYgK-Mtv-7-vaNnEC6wFNEzchkpAHU6M0KZ__RGcuuAWY9cSBClFiZmcc4CmHeO9GJJCjxau-gzPa9nEG7bvUkEFUGk4evu-ELPG4a9Nmna7JMVQ3eSry3SZnm0Z_uyzV7nUtHcWoD0Bc-xyuF5mt8NFm37PaHyaDLaypiwJ_HfoaWSNCucwuZfXTtZ76w_TvBToqOj9qo40zfOtOeYeQ`


## Permissions

get:movies
get:actors

post:actors
post:movies

delete:actors
delete:movies

patch:actors
patch:movies

## Roles
ofineo@gmail.com


Casting Assistant
    get:movies
    get:actors


ofineo@hotmail.com

Casting Director
    get:movies
    get:actors
    post:actors
    delete:actors
    patch:actors
    patch:movies


basura@outlook.jp

Executive producer
    get:movies
    get:actors
    post:actors
    post:movies
    delete:actors
    delete:movies
    patch:actors
    patch:movies


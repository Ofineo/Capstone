
## GET

`curl localhost:5000/movies`
`curl localhost:5000/actors`


## DELETE

`curl localhost:5000/movies/3 -X DELETE`
`curl localhost:5000/actors/3 -X DELETE`


## POST

`curl localhost:5000/movies/add -X POST -H"Content-Type: application/json" -d'{"title":"random title","releaseDate":"2020-03-25 11:55:11.271041","actor_id": ["1","2","4"]}' `

`curl localhost:5000/actors/add -X POST -H"Content-Type: application/json" -d'{"name":"pepe Gotera", "age":"45",gender":"male"}'`


## PATCH

`curl localhost:5000/actors/6 -X PATCH -H"Content-Type: application/json" -d'{"name":"Otilio", "age":"54"}'`

`curl localhost:5000/movies/5 -X PATCH -H"Content-Type: application/json" -d'{"title":"avengers vs godzilla","releaseDate":"2021-03-25 11:55:11.271041"}'`
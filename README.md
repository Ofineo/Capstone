
## GET

`curl localhost:5000/movies`
`curl localhost:5000/actors`


## DELETE

`curl localhost:5000/movies/3 -X DELETE`
`curl localhost:5000/actors/3 -X DELETE`


## POST

`curl localhost:5000/movies/add -X POST -H"Content-Type: application/json" -d"{'title':'random title', 'releaseDate':'2020-03-25 11:55:11.271041'}" `

`curl localhost:5000/actors/add -X POST -H"Content-Type: application/json" -d"{'name':'pepe Gotera', 'age':'45', 'gender':'male'}" `


## PATCH


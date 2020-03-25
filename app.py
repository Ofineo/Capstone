import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from  models import setup_db, Actor, Movie
import datetime


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  # cors = CORS(app, resources={r"127.0.0.1/*":{"origins":"*"}})

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,OPTIONS,PATCH')
    return response

  @app.route('/')
  def main():
    greeting = "Hi There" 
   
    return greeting

  @app.route('/actors')
  def get_actors():
    selection = Actor.query.all()

    actors = []

    for actor in selection:
      actors.append(actor.format())

    return jsonify({
      'status': True,
      'actors': actors
    })


  @app.route('/movies')
  def get_movies():
    selection = Movie.query.all()

    movies = []

    for movie in selection:
      movies.append(movie.format())

    return jsonify({
      'status': True,
      'movies': movies
    })

  @app.route('/actors/<id>', methods=['DELETE'])
  def delete_actor(id):
    selection = Actor.query.get(id)

    print(selection)

    if not selection:
      abort(404)
    
    try:
      selection.delete()
    except Exception as e:
      print('it could not be deleted', e)

    return jsonify({
      'status': True,
      'actor': id
    })


  @app.route('/movies/<id>', methods=['DELETE'])
  def movie(id):
    selection = Movie.query.get(id)

    print(selection)

    if not selection:
      abort(404)
    
    try:
      selection.delete()
    except Exception as e:
      print('it could not be deleted', e)

    return jsonify({
      'status': True,
      'movie': id
    })

  @app.route('/actors/add', methods=['POST'])
  def post_actor():
    res = request.get_json()
   
    if not res:
      abort(400)

    try:
      actor = Actor(
        name=res['name'],
        age=res['age'],
        gender=res['gender']
      )
      actor.insert()
     
    except Exception as e:
      print('we couldnt create the object', e)
      abort(500)
    return jsonify({
      'status': True,
      'actor': [actor.format()] 
      })


  @app.route('/movies/add', methods=['POST'])
  def post_movies():
    res = request.get_json()
   
    x = datetime.datetime(2020, 5, 17)
 
    if not res:
      abort(400)
      
    try:
      movie = Movie(
        title=res['title'],
        releaseDate=x,
        actor_id=res['actor_id']
        
      )
      movie.insert()
      
    except Exception as e:
      print('we couldnt create the object. Reason :', e)
      abort(500)

    return jsonify({
            'status': True,
            'movie': [movie.format()] 
          })

  @app.route('/actors/<id>', methods=['PATCH'])
  def patch_actors(id):
    res = request.get_json()

    if not res:
      abort(404)
    
    actor = Actor.query.get(id)
    
    try:
      if 'name' in res:
        actor.name=  res['name']
      if 'age' in res:
        actor.age=   res['age']
      if 'gender' in res:
        actor.gender=  res['gender']
      
      actor.update()

    except Exception as e:
      print('we couldnt create the object. Reason :', e)
      abort(500)

    return jsonify({
            'status': True,
            'actor': [actor.format()] 
          })

    
  @app.route('/movies/<id>', methods=['PATCH'])
  def patch_movies(id):
    res = request.get_json()

    if not res:
      abort(404)
    
    movie = Movie.query.get(id)
    
    try:
      if 'title' in res:
        movie.title=  res['title']
      if 'releaseDate' in res:
        movie.releaseDate=   res['releaseDate']
      if 'actor_id' in res:
        movie.actor_id=  res['actor_id']
      
      movie.update()

    except Exception as e:
      print('we couldnt create the object. Reason :', e)
      abort(500)

    return jsonify({
            'status': True,
            'movie': [movie.format()] 
          })

  
# Error Handling


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False,
                    "error": 422,
                    "message": "unprocessable."
                    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "The server can not find the requested resource."
    }), 404


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "You are no authorized."
    }), 401


  return app

# APP = create_app()

# if __name__ == '__main__':
#     APP.run(host='0.0.0.0', port=8080, debug=True)
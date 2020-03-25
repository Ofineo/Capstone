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
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,OPTIONS')
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
  







  return app

# APP = create_app()

# if __name__ == '__main__':
#     APP.run(host='0.0.0.0', port=8080, debug=True)
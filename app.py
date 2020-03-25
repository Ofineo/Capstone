import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from  models import setup_db, Actor, Movie


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


  return app

# APP = create_app()

# if __name__ == '__main__':
#     APP.run(host='0.0.0.0', port=8080, debug=True)
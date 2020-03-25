import os
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "Capstone"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()
'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


'''
Table Actors

'''


class Actor(db.Model):
    __tablename__ = 'actor'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    movie = relationship("Movie", back_populates="actor")

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    '''
     insert()
         inserts a new model into a database
         the model must have a unique id or null id
         the model must have a  name
         the model must have an age
         the model must have a gender
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
      update()
          updates a new model into a database
          the model must exist in the database
    '''

    def update(self):
        db.session.commit()

    '''
      delete()
          deletes a new model into a database
          the model must exist in the database
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
      format()
          form representation of the actor model
    '''

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }


'''
Table Actors
'''


class Movie(db.Model):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String(20), nullable=False)
    releaseDate = Column(DateTime(timezone=False), nullable=False)
    actor_id = Column(Integer, ForeignKey('actor.id'))
    actor = relationship("Actor", back_populates="movie")

    def __init__(self, title, releaseDate, actor_id):
        self.title = title
        self.releaseDate = releaseDate
        self.actor_id = actor_id

    '''
     insert()
         inserts a new model into a database
         the model must have a unique id or null id
         the model must have a  title
         the model must have a  releasedate
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
      update()
          updates a new model into a database
          the model must exist in the database
    '''

    def update(self):
        db.session.commit()

    '''
      delete()
          deletes a new model into a database
          the model must exist in the database
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
      format()
          form representation of the movie model
    '''

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release date': self.releaseDate,
            'actor_id': self.actor_id
        }

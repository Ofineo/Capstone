import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie
import datetime


class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "Capstone_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_actor = {
            'name':'John Smith', 
            'age': 34, 
            'gender': 'male', 
        }
        
        self.new_movie = {
            'actor_id': '2',
            'releaseDate': datetime.datetime(2022, 2, 22),
            'title': 'Contagion',
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
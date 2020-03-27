import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie
import datetime

TOKEN_PRODUCER = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9USXpNakl6UkVZMFJEQXdNRGN3UTBFNVF6TTBNekE0TURNMVF6bERRVGRFUVRNeE1VUXpNdyJ9.eyJpc3MiOiJodHRwczovL29maW5lby5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU3YzY4Y2ExMWRkNDkwYzZiM2VlNTM0IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1ODUzMDAyMjUsImV4cCI6MTU4NTM4NjYyNSwiYXpwIjoiMzVNNTJYbEgxM1R6NDl6T3gzQXBkUTdrNmY3Y1Fnb2wiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.WSJMNDMlOy7bkcJMePO1RKKSHpfcxdbcC_GCOepLKYgBRRfuuDUt76555m1ZD2V0FYlcicpquA0uqqvOXyt-4aepqbUvauI02zt-7aALae8cbYlqvulcSrPTzfON_wJu3YSdLjYtHbvoLg7zL-umTTI4Fozb63UPbQGb_rQD9IwU_ud8s7wb1mCSqpZzczNbI7FrYp2F-I5T1gEY3zvAOtygasC5d-jQ8t3mYRq4GJcROQ83bolkrI0fX4ynIxqow2vh89zBb6E8KZt1vly0IuocViK_4XRGr5fhLc4vgusjhdua-R4Pr6zjP4sTX4Mq-b16JfKGFvoUNh9DwpUOtw'

class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "Capstone_test"
        self.database_path = os.environ['TEST_DATABASE_URL']
        setup_db(self.app, self.database_path)

        self.new_actor = {
            'name': 'John Smith',
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
        selection = Movie.query.filter(Movie.title == 'Contagion').all()
        for movie in selection:
            movie.delete()
        selection = Actor.query.filter(Actor.name == 'John Smith').all()
        for actor in selection:
            actor.delete()
        pass

    def test_get_all_actors(self):
        res = self.client().get('/actors', headers={
            'Authorization': TOKEN_PRODUCER}
        )
        data = res.get_json()

        selection = Actor.query.all()

        self.assertEqual(data['status'], True)
        self.assertEqual(data['actors'], [actor.format() for actor in selection])

    def test_post_actor(self):
        table_length = Actor.query.all()

        res = self.client().post('/actors/add', headers={
            'Authorization': TOKEN_PRODUCER},
            json=self.new_actor
        )

        data = res.get_json()

        self.assertEqual(data['status'], True)
        self.assertGreater(len(Actor.query.all()), len(table_length))

    def test_patch_actor(self):
        actor = Actor(
            name='Otilio',
            age=22,
            gender='male'
        )
        actor.id = 222
        actor.insert()

        res = self.client().patch('/actors/222', headers={
            'Authorization': TOKEN_PRODUCER},
            json={
                "name": "Otilio", 
                "age": "54"
            }
        )
        data = res.get_json()

        actor = Actor.query.filter(Actor.id == 222).one_or_none()

        self.assertEqual(data['status'], True)
        self.assertEqual(actor.name, 'Otilio')

        actor.delete()

    def test_delete_actor(self):
        actor = Actor(
            name='Sean Conery',
            age=75,
            gender='male'
        )
        actor.id = 222
        actor.insert()

        res = self.client().delete('/actors/222', headers={
            'Authorization': TOKEN_PRODUCER},
        )

        data = res.get_json()
        selection = Actor.query.filter(Actor.id == 222).one_or_none()

        self.assertEqual(data['status'], True)
        self.assertEqual(selection, None)

    def test_get_all_movies(self):
        res = self.client().get('/movies', headers={
            'Authorization': TOKEN_PRODUCER}
            )
        data = res.get_json()

        selection = Movie.query.all()

        self.maxDiff = None

        self.assertEqual(data['status'], True)
        self.assertEqual(data['movies'], [movie.format() for movie in selection])

    def test_post_movie(self):
        table_length = Movie.query.all()

        res = self.client().post('/movies/add', headers={
            'Authorization': TOKEN_PRODUCER},
            json=self.new_movie
        )

        data = res.get_json()

        self.assertEqual(data['status'], True)
        self.assertGreater(len(Movie.query.all()), len(table_length))

    def test_patch_movie(self):
        movie = Movie(
            title='The cube',
            releaseDate=datetime.datetime(2022, 2, 22),
            actor_id='1'
        )
        movie.id = 222
        movie.insert()

        res = self.client().patch('/movies/222', headers={
            'Authorization': TOKEN_PRODUCER},
            json={
                "title": "avengers vs godzilla", 
                "releaseDate": "2021-03-25 11:55:11.271041"
            }
        )

        data = res.get_json()
        selection = Movie.query.filter(Movie.id == 222).one_or_none()

        self.assertEqual(data['status'], True)
        self.assertEqual(selection.title, 'avengers vs godzilla')

        selection.delete()

    def test_delete_movie(self):
        movie = Movie(
            title='The cube',
            releaseDate=datetime.datetime(2022, 2, 22),
            actor_id='1'
        )
        movie.id = 222
        movie.insert()

        res = self.client().delete('/movies/222', headers={
            'Authorization': TOKEN_PRODUCER},
        )

        data = res.get_json()
        selection = Movie.query.filter(Movie.id == 222).one_or_none()

        self.assertEqual(data['status'], True)
        self.assertEqual(selection, None)

# Make the tests conveniently executable


if __name__ == "__main__":
    unittest.main()

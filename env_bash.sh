
export AUTH0_DOMAIN='ofineo.eu.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='capstone'
export DATABASE_URL="postgres://postgres:password!@localhost:2345/capstone_docker"
export FLASK_APP=app.py
export FLASK_DEBUG=true
flask run --reload

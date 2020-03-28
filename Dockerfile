FROM python:3.7.2

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV AUTH0_DOMAIN='ofineo.eu.auth0.com' \
    ALGORITHMS=['RS256'] \
    API_AUDIENCE='capstone' \
    DATABASE_URL="postgres://postgres:password!@172.17.0.2:5432/capstone_docker"


ENTRYPOINT ["gunicorn", "-b", ":8080", "app:APP"]
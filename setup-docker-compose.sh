#!/bin/sh

set -ea

docker-compose up -d database
docker-compose build webserver
docker-compose run webserver python manage.py migrate
docker-compose run webserver python manage.py importwordlist words.txt
echo ""
echo "Press ctrl-c to skip user creation"
echo ""
docker-compose run webserver python manage.py createsuperuser || true

echo ""
echo "Run the following command to start the server at http://localhost:8000"
echo "$ docker-compose up webserver"
echo ""

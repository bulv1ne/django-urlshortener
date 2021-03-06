# django-urlshortener
An example django project with docker-compose

## Requirements

- docker
- docker-compose

## Install

Execute the `setup-docker-compose.sh` script to:
- Start the postgres database in the background
- Build the webserver
- Install the django migrations
- Import a wordlist for the urlshortener application
- Create an admin user (press Ctrl-C to cancel)

```sh
$ ./setup-docker-compose.sh
```

## Run the webserver

```sh
$ docker-compose up webserver
```

## Web endpoints

- http://localhost:8000/ the main webpage
- http://localhost:8000/api/shorturl/ POST to create a short url
- http://localhost:8000/api/schema/ OpenAPIv3 config file
- http://localhost:8000/api/schema/swagger-ui/ Swagger UI for the api documentation

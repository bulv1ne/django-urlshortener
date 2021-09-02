#!/bin/bash

set -eax

python manage.py migrate

gunicorn -b 0.0.0.0:8000 -t 60 server.asgi -k uvicorn.workers.UvicornWorker --log-config /var/gunicorn.logconfig

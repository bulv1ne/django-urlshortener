FROM python:3.9-slim

RUN pip install -U pip poetry
COPY pyproject.toml poetry.lock /var/
WORKDIR /var/

RUN poetry config virtualenvs.create false && poetry install
COPY src /var/project
WORKDIR /var/project

ENV STATIC_ROOT /var/static_root
RUN mkdir /var/static_root
RUN python manage.py collectstatic --no-input
COPY run.sh gunicorn.logconfig /var/

RUN useradd -s /bin/bash user
USER user

EXPOSE 8000

CMD ["/var/run.sh"]

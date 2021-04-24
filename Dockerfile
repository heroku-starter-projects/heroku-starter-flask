FROM python:3.6-alpine

# install dependencies
RUN apk --update add gcc python-dev linux-headers musl-dev postgresql-dev build-base
RUN pip install pipenv gunicorn

# prepare app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install project dependencies
COPY Pipfile* ./
RUN set -ex && pipenv install --deploy --system

# copy sources
COPY . .

# tells Makefile to use system python instead of pipenv
ENV PIPENV_IN_DOCKER=1

# starting service
CMD [ "gunicorn", "-c", "wsgi.conf.py", "server:app" ]

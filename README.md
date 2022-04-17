# heroku-starter-flask

## Installation

### Environment setup

1. Make sure `pipenv` and `make` are installed.
2. Run `make install`
3. Copy the `.env_sample` to `.env` and edit values if necessary
4. Run `docker compose up` to start the postgres DB
5. Run `pipenv shell` if shell doesnt open automatically.

### Run existing migrations

```sh
make db-upgrade
```

### Create new migrations

```sh
pipenv run alembic revision --autogenerate -m "Add users table"
```

## Running

1. For debug mode run `make watch`. For non-debug run `make run`
2. Import `./postman/*` into postman to get the API docs.

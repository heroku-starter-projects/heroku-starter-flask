# flake8: noqa: E501
from os import environ


class Config:
    # Server config
    HOST = environ.get("SERVER_HOST", "0.0.0.0")
    PORT = int(environ.get("SERVER_PORT", 5000))
    CONCURRENCY = (
        int(environ.get("CONCURRENCY")) if environ.get("CONCURRENCY") else None
    )
    ENV = environ.get("ENV", "production")

    # Logging
    DEBUG = int(environ.get("DEBUG", 0))
    LOG_LEVEL = environ.get("LOG_LEVEL", "INFO")

    # DB connection
    DB_USERNAME = environ.get("DB_USERNAME")
    DB_PASSWORD = environ.get("DB_PASSWORD")
    DB_NAME = environ.get("DB_NAME")
    DB_HOST = environ.get("DB_HOST")
    DB_PORT = environ.get("DB_PORT", 5432)
    DB_SSL_MODE = environ.get("DB_SSL_MODE")

    # JWT secrets
    JWT_SECRET = environ.get("JWT_SECRET")
    JWT_ALGORITHM = "HS256"

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app import Config


def sqlalchemy_session(pg_connection_string):
    sslmode = Config.DB_SSL_MODE
    echo = Config.ENV == "development"

    # https://stackoverflow.com/a/25095643/1217998
    engine = create_engine(
        pg_connection_string, connect_args={"sslmode": sslmode}, echo=echo
    )
    return scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def generate_connection_string():
    host = Config.DB_HOST
    port = Config.DB_PORT
    username = Config.DB_USERNAME
    password = Config.DB_PASSWORD
    db = Config.DB_NAME

    # https://stackoverflow.com/a/64698899/1217998
    return f"postgresql://{username}:{password}@{host}:{port}/{db}"

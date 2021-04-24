from flask import g
from werkzeug.exceptions import BadRequest

# from app import logger
from app.helpers.database import generate_connection_string, sqlalchemy_session


def register_database_hook(app):
    @app.before_request
    def before_request():
        try:
            pg_connection_string = generate_connection_string()
            g.session = sqlalchemy_session(pg_connection_string)
        except Exception as e:
            # logger.warn('Unable to get database secret', exc_info=e)
            raise BadRequest('Unable to connect to DB')

    @app.teardown_appcontext
    def teardown_appcontext(_e):
        if 'session' in g:
            g.session.remove()

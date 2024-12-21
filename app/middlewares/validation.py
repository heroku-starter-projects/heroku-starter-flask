from marshmallow import Schema, ValidationError
from flask import request, g
from werkzeug.exceptions import BadRequest
from functools import wraps

# from app import logger


def validate_json(schema):
    """
    Validation decorator for the request json body

    Example usage:

        from flask import g
        from marshmallow import Schema, fields
        from app.router.middleware import validate_body

        class SomeResource(Resource):

            class SomeRequestSchema(Schema):
                some_str = fields.Str(required=True)

            @staticmethod
            @validate_json(SomeRequestSchema())
            def post():
                # Use g.json here
    """

    def deco(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            g.json = _validate_data(
                request.get_json(force=True, silent=True), schema, "body"
            )
            return f(*args, **kwargs)

        return wrapped

    return deco


def validate_query(schema):
    """
    Validation decorator for the request query args
    """

    def deco(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            g.args = _validate_data(request.args, schema, "query")
            return f(*args, **kwargs)

        return wrapped

    return deco


def validate_url(schema):
    """
    Validation decorator for the request url variables
    """

    def deco(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            g.vars = _validate_data(kwargs, schema, "url")
            return f(*args, **kwargs)

        return wrapped

    return deco


def _validate_data(data, schema, input_type):
    """
    Validate data again schema and raise if data is invalid
    """
    assert isinstance(schema, Schema)
    try:
        result = schema.load(data)
    except ValidationError as err:
        raise BadRequest(description=f"Invalid {input_type} parameters: {err.messages}")
    return result

# from flask import g
from flask_restful import Resource
from marshmallow import Schema, fields, validate

from app.middlewares.validation import validate_json
# from app.models import User as UserModel


class LoginRequestSchema(Schema):
    email = fields.Str(required=True, validate=validate.Length(min=1, max=120))
    password = fields.Str(required=True, validate=validate.Length(min=1))


class Login(Resource):

    @validate_json(LoginRequestSchema())
    def post(self):
        # TODO
        return {'message': 'Success'}

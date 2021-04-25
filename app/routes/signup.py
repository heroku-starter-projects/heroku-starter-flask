from flask import g
from flask_restful import Resource
from marshmallow import Schema, fields, validate

from app.middlewares.validation import validate_json
from app.models import User as UserModel


class SignupRequestSchema(Schema):
    email = fields.Str(required=True, validate=validate.Length(min=1, max=120))
    name = fields.Str(required=True, validate=validate.Length(min=1))
    password = fields.Str(required=True, validate=validate.Length(min=1))


class Signup(Resource):

    @validate_json(SignupRequestSchema())
    def post(self):
        user = UserModel(g.json['email'], g.json['name'], g.json['password'])
        g.session.add(user)
        g.session.commit()
        return user.dump(), 201

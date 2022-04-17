from flask import g
from flask_restful import Resource
from marshmallow import Schema, fields, validate
import flask_bcrypt as bcrypt

from app.middlewares.validation import validate_json
from app.models import User as UserModel


class SignupRequestSchema(Schema):
    email = fields.Str(required=True, validate=validate.Length(min=1, max=120))
    name = fields.Str(required=True, validate=validate.Length(min=1))
    password = fields.Str(required=True, validate=validate.Length(min=1))


class Signup(Resource):

    @validate_json(SignupRequestSchema())
    def post(self):
        # https://stackoverflow.com/a/38262440/1217998
        password = g.json['password']
        hashed_password = bcrypt.generate_password_hash(password.encode('utf8')).decode('utf8')
        user = UserModel(g.json['email'], g.json['name'], hashed_password)
        g.session.add(user)
        g.session.commit()
        g.user = user

        return {'message': 'Sign up successful', 'code': 'SIGNUP_SUCCESS'}, 201

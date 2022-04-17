from flask import g
from flask_restful import Resource
from marshmallow import Schema, fields, validate
import flask_bcrypt as bcrypt

from app.middlewares.validation import validate_json
from app.models import User as UserModel

from werkzeug.exceptions import Unauthorized


class LoginRequestSchema(Schema):
    email = fields.Str(required=True, validate=validate.Length(min=1, max=120))
    password = fields.Str(required=True, validate=validate.Length(min=1))


class Login(Resource):

    @validate_json(LoginRequestSchema())
    def post(self):
        maybe_user = g.session.query(UserModel).filter_by(email=g.json['email']).first()

        if maybe_user is None:
            # Dont let the attacker know whether a user exists or not
            raise Unauthorized()

        if not bcrypt.check_password_hash(maybe_user.password, g.json['password'].encode('utf8')):
            raise Unauthorized()

        g.user = maybe_user

        return {'message': 'Success', 'code': 'LOGIN_SUCCESS'}

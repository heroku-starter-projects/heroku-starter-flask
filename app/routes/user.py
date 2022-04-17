from flask import g
from flask_restful import Resource

from app.middlewares.auth import requires_auth
from app.models import User as UserModel


class User(Resource):

    @requires_auth
    def get(self, user_id=None):
        user = g.user

        # TODO: Check if admin
        if user_id is not None:
            user = g.session.query(UserModel).get(user_id)

        return {
            'name': user.name,
            'email': user.email,
        }

from flask import g
from flask_restful import Resource

from app.middlewares.auth import requires_auth
from app.models import User as UserModel


class User(Resource):

    @requires_auth
    def get(self, user_id):
        user = g.session.query(UserModel).get(user_id)
        return user.dump()

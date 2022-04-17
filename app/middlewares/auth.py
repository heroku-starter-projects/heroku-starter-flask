from functools import wraps
from flask import g
import jwt
from werkzeug.exceptions import Unauthorized, NotFound
from app.config import Config

from app.models.user import User as UserModel


def requires_auth(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        try:
            obj = jwt.decode(g.token, key=Config.JWT_SECRET, algorithms=Config.JWT_ALGORITHM)
            user_id = obj['sub']
        except Exception as e:
            print(e, g.token)
            raise Unauthorized()

        user = g.session.query(UserModel).get(user_id)

        if user is None:
            raise NotFound()

        g.user = user

        return f(*args, **kwargs)

    return wrapped

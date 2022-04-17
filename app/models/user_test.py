import unittest

import jwt
from app.config import Config

from app.models.user import User


class UserTestCase(unittest.TestCase):

    # python -m unittest app.models.user_test.UserTestCase.test_100_jwt_encode
    def test_100_jwt_encode(self):
        user = User(email='a@b.com', name='foo', password='bar')
        user.id = 1

        token = user.generate_token()
        user_obj = jwt.decode(token, key=Config.JWT_SECRET, algorithms=Config.JWT_ALGORITHM)

        assert user.id == user_obj['sub']

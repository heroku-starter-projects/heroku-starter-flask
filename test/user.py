from app.config import Config
from test import AppTestCase
import jwt


# pipenv run python -m unittest test.user.UserTestCase
class UserTestCase(AppTestCase):
    @classmethod
    def setUpClass(cls):
        super(UserTestCase, cls).setUpClass()
        cls.user = {
            'email': 'a@b.com',
            'name': 'Foo',
            'password': 'bar',
        }

    # pipenv run python -m unittest test.user.UserTestCase.test_100_create_user
    def test_100_create_user(self):
        response = self.app.post('/signup', json=self.user)
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json, dict)
        obj = jwt.decode(
            response.json['token'], key=Config.JWT_SECRET, algorithms=Config.JWT_ALGORITHM)
        self.assertIsInstance(obj['sub'], int)
        self.assertIsInstance(obj['iat'], int)
        self.assertIsInstance(obj['exp'], int)

    # def test_110_get_user(self):
    #     rv = self.app.get('/user')
    #     self.assertEqual(rv.status_code, 200)
    #     self.assertIsInstance(rv.json, dict)
    #     self.assertIsInstance(rv.json['user'], list)
    #     self.assertGreaterEqual(len(rv.json['user']), 1)
    #     user = [
    #         user for user in rv.json['user']
    #         if user['title'] == self.user['title']
    #     ]
    #     self.assertEqual(len(user), 1)
    #     self.assertEqual(user[0]['title'], self.user['title'])
    #     self.assertEqual(user[0]['body'], self.user['body'])

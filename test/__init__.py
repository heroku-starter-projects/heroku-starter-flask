import unittest
import warnings
from alembic import command
from alembic.config import Config

from app import create_app

app = create_app()
alembic_cfg = Config("alembic.ini")


class AppTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore")
        app.testing = True

        command.upgrade(alembic_cfg, 'head', tag='test')

    @classmethod
    def tearDownClass(cls):
        command.downgrade(alembic_cfg, 'base', tag='test')

    def setUp(self):
        # App context
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

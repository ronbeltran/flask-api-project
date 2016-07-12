from flask import current_app

from tests.base import BaseTestCase


class TestingSetupTestCase(BaseTestCase):

    def test_app_exist(self):
        self.assertIsNotNone(current_app)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config["TESTING"])

    def test_database_name_for_testing(self):
        self.assertIn("test_", current_app.config["DATABASE_NAME"])
        self.assertIn(current_app.config["DATABASE_NAME"], current_app.config["SQLALCHEMY_DATABASE_URI"])

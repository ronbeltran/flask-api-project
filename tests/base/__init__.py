import unittest

from app import create_app, db


class BaseTestCase(unittest.TestCase):

    def ensure_using_test_database(self):
        """
        Testing Checkpoint. Testing can deliberately destroy
        local development database and its content.
        Also can mess with the alembic version set in the DB.
        """
        assert self.app.config["TESTING"] is True, Exception("Wrong config. TESTING is False")
        assert "test_" in self.app.config["DATABASE_NAME"], Exception("Wrong database name for testing.")

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.ensure_using_test_database()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

#!/usr/bin/env python
import os

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db


app = create_app(os.environ.get("FLASK_CONFIG", "default"))
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app)


@manager.command
def test():
    """ Run the unit tests """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()

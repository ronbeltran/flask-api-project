from flask import Flask

from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from accounts import accounts as accounts_blueprint
    app.register_blueprint(accounts_blueprint)

    return app

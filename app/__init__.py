from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # initializations
    db.init_app(app)

    # routes
    from accounts import accounts as accounts_blueprint
    app.register_blueprint(accounts_blueprint)

    from accounts.rest import accounts_api_blueprint
    app.register_blueprint(accounts_api_blueprint, url_prefix="/v1/api/accounts")

    return app

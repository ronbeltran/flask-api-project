from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT

from config import config
from accounts.jwt_helper import jwt_authenticate
from accounts.jwt_helper import jwt_identity

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # initializations
    db.init_app(app)
    jwt = JWT(app, jwt_authenticate, jwt_identity)  # noqa

    # routes
    from accounts import accounts as accounts_blueprint
    app.register_blueprint(accounts_blueprint)

    from accounts.rest import accounts_api_blueprint
    app.register_blueprint(accounts_api_blueprint, url_prefix="/v1/api/accounts")

    return app

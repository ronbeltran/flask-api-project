from flask import Blueprint
from flask_restful import Api

from .views import HelloView


accounts_api_blueprint = Blueprint("accounts_api", __name__)
accounts_api = Api(accounts_api_blueprint)

accounts_api.add_resource(HelloView, "/hello", endpoint="accounts_hello")

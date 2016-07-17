from flask import g
from flask_restful import Resource
from flask_jwt import jwt_required


class HelloView(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        return g.user.to_json()

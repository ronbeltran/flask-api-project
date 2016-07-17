from flask_restful import Resource
from flask_jwt import current_identity

from flask import g

from ..jwt_helper import jwt_login_required


class HelloView(Resource):
    method_decorators = [jwt_login_required]

    def get(self):
        print current_identity
        print g.user_id
        print g.user
        return {"message": "OK"}

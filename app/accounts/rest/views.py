from flask_restful import Resource


class HelloView(Resource):

    def get(self):
        return {"message": "OK"}

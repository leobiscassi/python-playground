from flask_restful import Resource

class Hello(Resource):
    def get(self):
        return {"GET - message" : "Hello world!"}
    def post(self):
        return {"POST - message" : "Hello world!"}
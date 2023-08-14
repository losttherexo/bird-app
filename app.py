from flask import jsonify, make_response
from flask_restful import Resource

from config import api, app
from models import db, Bird

class Home(Resource):
    def get(self):
        return 'Yes this works, go to /birds ;)'

class Birds(Resource):

    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds), 200)

api.add_resource(Home, '/')
api.add_resource(Birds, '/birds')
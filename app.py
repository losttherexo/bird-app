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
    
class BirdByID(Resource):
    def get(self, id):
        bird = Bird.query.filter_by(id=id).first().to_dict()
        return make_response(jsonify(bird), 200)

api.add_resource(Home, '/')
api.add_resource(Birds, '/birds')
api.add_resource(BirdByID, '/birds/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
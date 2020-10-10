# d:\Pycode\Pytw_A01\flask_01.py

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world', 'happy': 'everyday'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

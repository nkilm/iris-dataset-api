from flask import Flask, jsonify
from flask_restful import Resource, Api,reqparse
import pickle
import json
import numpy as np
import constants as const


app = Flask(__name__)
api = Api(app)

# Create parser for the payload data
parser = reqparse.RequestParser()
parser.add_argument('data')

info = {
    0:"Iris-Setosa",
    1:"Iris-Versicolour",
    2:"Iris-Virginica"
}
class Info(Resource):
    def get(self):
        return jsonify({"/":"An example for ML Model API(Iris Dataset)"})
class Iris(Resource):
    def get(self):
        return jsonify(info)
    def post(self):
        args = parser.parse_args()
        values =  json.loads(args['data'])

        X = np.array(values).reshape(1,-1)
        prediction = model.predict(X)
        
        return jsonify(info.get(prediction[0]))


api.add_resource(Info, '/')
api.add_resource(Iris,'/iris')

if __name__ == '__main__':
    with open("models/iris_lr.sav","rb") as f:
        model = pickle.load(f)
    app.run(debug=True,port=const.PORT)
    
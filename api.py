from flask import Flask
from flask_restful import Resource, Api,reqparse

app = Flask(__name__)
api = Api(app)

# Create parser for the payload data
parser = reqparse.RequestParser()
parser.add_argument('data')

class Info(Resource):
    def get(self):
        return "An example for ML Model API(Iris Dataset)"

class Iris(Resource):
    def post(self):
        args = parser.parse_args()
        X = np.array(json.loads(args['data']))
        prediction = model.predict(X)
        return jsonify(prediction.tolist())

api.add_resource(Info, '/')

if __name__ == '__main__':
    app.run(debug=True,port=5050)
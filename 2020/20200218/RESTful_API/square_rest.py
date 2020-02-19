from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


class Index(Resource):
    def get(self):
        return {'data': 'Hello World!'}


class Square(Resource):
    def get(self, num):
        # curl -v http://localhost:8080/square/3
        return {'result': num**2}, 201


class Square2(Resource):
    def get(self):
        # curl -v http://localhost:8080/square?num=3
        parser = reqparse.RequestParser()
        parser.add_argument('num', type=int, help='Number to square')
        args = parser.parse_args()
        num = int(args.get('num'))
        return {'args_result': num**2}

    def post(self):
        # curl -H "Content-Type: application/json" -X POST -d '{"num":"5"}' http://localhost:8080/square
        parser = reqparse.RequestParser()
        parser.add_argument('num', type=int, help='Number to square')
        args = parser.parse_args()
        num = int(args.get('num'))
        return {'args_result': num**2}


api.add_resource(Index, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(Square2, '/square')


if __name__ == "__main__":
    app.run(port=8080)

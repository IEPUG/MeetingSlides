from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'data': 'Hello World!'})


@app.route('/square/<int:num>', methods=['GET'])
def get_square(num):
    return jsonify({'result': num**2})


@app.route('/square', methods=['GET'])
def get_square2():
    num = int(request.args.get('num'))
    return jsonify({'args_result': num**2})


if __name__ == "__main__":
    app.run(port=8080)

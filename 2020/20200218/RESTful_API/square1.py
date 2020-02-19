from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'data': 'Hello World!'})


@app.route('/square/<int:num>', methods=['GET'])
def get_square(num):
    return jsonify({'result': num**2})


if __name__ == "__main__":
    app.run(port=8080)

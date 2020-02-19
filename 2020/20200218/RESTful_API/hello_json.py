from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'data': 'Hello World!'})


@app.route('/add_customer')
def add_data():
    return make_response(jsonify({'result': 'customer added'}), 201)


if __name__ == "__main__":
    app.run(port=8080)

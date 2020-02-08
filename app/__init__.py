from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/EUS')
def departures():
    return jsonify(
        train='LATE!'
    )


if __name__ == '__main__':
    app.run()

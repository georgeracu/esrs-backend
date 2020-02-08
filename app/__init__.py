from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/EUS')
def departures():
    return jsonify(
        station='London Euston',
        std='16:07',
        etd='16:30'
    )


if __name__ == '__main__':
    app.run()

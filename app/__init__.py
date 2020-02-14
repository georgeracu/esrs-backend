import json

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Test!'


@app.route('/departures/EUS')
def departures():
    """Return a JSON object of mock departures from Euston Station

    :return: A valid JSON of departures
    """
    with open('./test/mocks/euston_response.json') as json_file:
        data = json.load(json_file)
        return data


if __name__ == '__main__':
    app.run()

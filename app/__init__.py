from flask import Flask

import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/departures/<crs>')
def get_departures(crs):
    """Gets the departure times from a station's CRS (Computer Reservation System) code. Examples can be seen [here](
    https://rail-record.co.uk/railway-location-codes/)

    :param crs: the CRS code of the station
    :return: a JSON of departures from station code CRS, or an HTTP error if the CRS is invalid.
    """
    load_dotenv()
    national_rail_api_key = os.getenv('TRAIN_API_KEY')

    base_url = 'https://api.departureboard.io/api/v2.0/getDeparturesByCRS/' + crs
    payload = {'apiKey': national_rail_api_key, 'serviceDetails': 'false'}
    r = requests.get(base_url, payload)
    if r.status_code == 400:
        return "Error: not a valid CRS", r.status_code
    return r.json()


if __name__ == '__main__':
    app.run()

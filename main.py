from flask import Flask, jsonify
from api_consumer import stations_data as stations

app = Flask(__name__)


if __name__ == '__main__':
    # app.run(port=8090, debug=True)
    stations.get_stations_by_range_filtered(12, 23, 10, station_name=['BP'])

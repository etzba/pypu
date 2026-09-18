import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from utils.utils import (
    setup_logger,
)
from locations.locations import (
    Location,
)

logger=setup_logger()
PORT=int(os.getenv("PORT"))

app = Flask(__name__)

@app.route('/locations', methods=(['GET']))
def get_locations_endpoint():
    data = Location.get_locations()
    resp = {
        "locations": data,
    }
    return jsonify(resp), 200

@app.route('/locations', methods=(['POST']))
def post_locations_endpoint():
    data = request.get_json()
    resp = post_location(data)
    return jsonify(resp), 201

if __name__ == '__main__':
    logger.info(f'Start listening in port {PORT}')
    app.run(port=PORT,host="0.0.0.0")
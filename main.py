import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

PORT=int(os.getenv("PORT"))

app = Flask(__name__)

@app.route('/locations', methods=(['GET']))
def get_locations_endpoint():
    data = ['some','location','somewhere','far','away']
    resp = {
        "locations": data,
    }
    return jsonify(resp), 200

@app.route('/locations', methods=(['POST']))
def post_locations_endpoint():
    data = request.get_json()
    resp = {
        "name": data('name'),
        "address": data('address'),
    }
    return jsonify(resp), 201

if __name__ == '__main__':
    app.run(port=PORT,host="0.0.0.0")
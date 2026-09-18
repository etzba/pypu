curl GET http://localhost:5000/locations

curl -X POST http://localhost:5000/locations \
    -H 'Content-Type: application/json' \ 
    -d '{ "name": "Etz", "address": "Davrewasdf",  "longtitude": 34.43212123, "latitude": 12.321312234 }'
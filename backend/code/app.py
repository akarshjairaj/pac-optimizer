#!flask/bin/python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'

@app.route('/get_container', methods=['GET', 'POST'])
def get_truck_id():
    json = request.get_json()
    print (json)
    #call the function to get the response json
    response_json = {"container_id": "container 1"}
    return jsonify(response_json)

if __name__ == '__main__':
    app.run(debug=True)
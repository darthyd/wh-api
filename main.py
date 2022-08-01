import json
import os
from flask import Flask, request
from scrap import getData
app = Flask(__name__)

gameList = []


@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'


@app.route('/api/scrap', methods=['GET'])
def scrap():
    getData(gameList)
    return json.dumps('Data request successfully')


@app.route('/api/games', methods=['GET'])
def games():
    return json.dumps(gameList)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)

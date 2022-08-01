import json
import os
from flask import Flask, request
from scrap import gamelist
from scrap2 import getData
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'


@app.route('/api/req/games', methods=['GET'])
def search_req():
    return json.dumps(gamelist)


@app.route('/api/sel/games')
def search_sel():
    return json.dumps(getData())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)

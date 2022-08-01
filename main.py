import json
import os
from flask import Flask, request
from scrap import gamelist
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'


@app.route('/api/games', methods=['GET'])
def search():
    return json.dumps(gamelist)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)

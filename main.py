import json
import os
from flask import Flask, redirect, request, send_from_directory, url_for
# from scrap import getData
app = Flask(__name__, static_url_path='/static/')

gameList = []


@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'

# @app.route('/api/scrap', methods=['GET'])
# def scrap():
#     getData()
#     return json.dumps('Data request successfully')


@app.route('/api/games', methods=['GET'])
def games():
    # if(len(gameList) == 0):
    return json.dumps('No data available')
    # return json.dumps(gameList)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)

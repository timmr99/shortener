#! /usr/bin/env python3
#
# This code is written in a Python 3.8.5 virtual environment
#
from shortener_app.utils import *

from flask import Flask
from flask import make_response, jsonify
import shortuuid


app = Flask(__name__)
app.url_map.strict_slashes = False # allow slashes '/' in request

db_name = 'shortened.json'

base_url = 'http://127.0.0.1:5000/'

# provide health request
@app.route('/', methods=['GET'])
def i_am_alive():
    return 'Good'

# provide version request
@app.route('/version', methods=['GET'])
def current_version():
    return '0.0.1'

@app.route('/<id>', methods=['GET'])
def expand(id):
    return ('expand {}'.format(id))

@app.route('/url=<path:url>', methods=['POST'])
def shorten(url):
    if url == 'url=':
        # return error, no id specified
        resp = make_response('No url specified', 400)
        return resp
    else:
        db = get_database(db_name)

        short = shortuuid.uuid(name=url)

        print('before: {}'.format(db))
        if db.get(short) == None:
            db[short] = url
            write_database(db_name, db)

        if db.get(url) == None:
            db[url] = short
            write_database(db_name, db)

        print('after: {}'.format(db))

        return (base_url + '{}'.format(short))



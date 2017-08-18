#!/usr/bin/env python
# -*- coding: utf-8 -*-
# app.py

from flask import Flask, request
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
	return 'Error : URI vacía'

@app.after_request
def apply_caching(response):
    response.headers["Server"] = "Python; Ubuntu; Flask; Werkzeug;"
    return response

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5001)
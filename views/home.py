#!/usr/bin/env python
# -*- coding: utf-8 -*-
# views/distrito.py
import json
from flask import Blueprint, request, render_template
from configs.helper import Helper

home = Blueprint('index', __name__)

@home.route('/', methods=['GET'])
def index():
	data = {'css' : 'vendor.min.css', 'js' : 'geo.min.js'} 
	return render_template('home/index.html', helper = Helper(), data = data), 200


@home.route('/subir', methods=['POST'])
def subir():
	file = request.files['myFile']
	file.save('/home/pepe/Descargas/flaskupload/Distritos_Expuestos.shp')

	return 'subir'
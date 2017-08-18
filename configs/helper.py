#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from .services import servicios

class Helper:
	def __init__(self):
		self.diccionario = {
			'BASE_URL': 'http://localhost:5000/',
			'STATIC_URL' : 'http://localhost:5000/static/',
			'ambiente': 'desarrollo',
			'nombre_app' : 'Aplicación Flask Boilerplate',
			'cipher_key' : 's53hHaKFQoqXTDU9',
			'servicios' : servicios 
		}

	def set(self, key, value):
		self.diccionario[key] = value

	def get(self, key):
		return self.diccionario[key]
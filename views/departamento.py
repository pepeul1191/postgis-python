#!/usr/bin/env python
# -*- coding: utf-8 -*-
# views/departamento.py
from flask import Blueprint
from configs.models import Departamento
from configs.helper import Helper

departamento = Blueprint('departamento', __name__)

@departamento.route('/departamento/listar')
def listar():
	#	print Helper().get('servicios')['accesos']
	#return render_template('departamento/timeline.html')
	return "departamento/listar"
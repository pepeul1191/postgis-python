#!/usr/bin/env python
# -*- coding: utf-8 -*-
# views/departamento.py
import json
from flask import Blueprint
from sqlalchemy.sql import select
from configs.models import Departamento
from configs.database import engine
from configs.helper import Helper

departamento = Blueprint('departamento', __name__)

@departamento.route('/departamento/listar')
def listar():
	#	print Helper().get('servicios')['accesos']
	#return render_template('departamento/timeline.html')
	conn = engine.connect()
	stmt = select([Departamento])
	return json.dumps([dict(r) for r in conn.execute(stmt)])
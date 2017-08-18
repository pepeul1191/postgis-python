#!/usr/bin/env python
# -*- coding: utf-8 -*-
# views/distrito.py
import json
from flask import Blueprint, request
from sqlalchemy.sql import select
from configs.models import Distrito, VWDistritoProvinciaDepartamento as VW
from configs.database import engine
from configs.helper import Helper

distrito = Blueprint('distrito', __name__)

@distrito.route('/distrito/listar/<int:provincia_id>', methods=['GET'])
def listar(provincia_id):
	conn = engine.connect()
	stmt = select([Distrito]).where(Distrito.provincia_id == provincia_id)
	rpta = []
	for r in conn.execute(stmt):
		rpta.append({'id':r[0], 'nombre':str(r[1])})
	return json.dumps(rpta)

@distrito.route('/distrito/buscar', methods=['GET'])
def vw_distrito_provincia_departamento_buscar():
	conn = engine.connect()
	stmt = select([VW]).where(VW.nombre.like(request.args.get('nombre') + '%' )).limit(10)
	return json.dumps([dict(r) for r in conn.execute(stmt)])
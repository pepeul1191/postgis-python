#!/usr/bin/env python
# -*- coding: utf-8 -*-
# views/provincia.py
import json
from flask import Blueprint
from sqlalchemy.sql import select
from configs.models import Provincia
from configs.database import engine
from configs.helper import Helper

provincia = Blueprint('provincia', __name__)

@provincia.route('/provincia/listar/<int:departamento_id>')
def listar(departamento_id):
	conn = engine.connect()
	stmt = select([Provincia.id, Provincia.nombre]).where(Provincia.departamento_id == departamento_id)
	return json.dumps([dict(r) for r in conn.execute(stmt)])
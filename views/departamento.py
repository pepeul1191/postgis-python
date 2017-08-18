#!/usr/bin/env python
# -*- coding: utf-8 -*-
# views/departamento.py
from flask import Blueprint, render_template
from configs.models import Departamento

departamento = Blueprint('departamento', __name__)

@departamento.route('/departamento/listar')
def listar():
    #return render_template('departamento/timeline.html')
    return "departamento/listar"
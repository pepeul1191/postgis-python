#!/usr/bin/env python
# -*- coding: utf-8 -*-
# views/departamento.py
from flask import Blueprint, render_template
from configs.models import Provincia

provincia = Blueprint('provincia', __name__)

@provincia.route('/provincia/listar/<int:departamento_id>')
def listar(departamento_id):
    #return render_template('provincia/timeline.html')
    return "provincia/listar"
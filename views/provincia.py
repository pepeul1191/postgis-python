#!/usr/bin/env python
# -*- coding: utf-8 -*-
# views/departamento.py
from flask import Blueprint, render_template

provincia = Blueprint('provincia', __name__)

@provincia.route('/provincia/listar')
def listar():
    #return render_template('provincia/timeline.html')
    return "provincia/listar"
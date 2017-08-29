#!/usr/bin/env python
# -*- coding: utf-8 -*-
# views/distrito.py
import json
from flask import Blueprint, request, render_template
from configs.helper import Helper

home = Blueprint('index', __name__)

@home.route('/', methods=['GET'])
def index():
    return render_template('home/index.html', helper = Helper()), 200
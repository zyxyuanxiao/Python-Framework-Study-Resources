# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 下午7:36
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

home = Blueprint('home', __name__)

import app.home.views

# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 上午9:37
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : exts.py
# @Software: PyCharm

from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

db = SQLAlchemy()
auth = HTTPBasicAuth()
auth2 = HTTPTokenAuth(scheme='Bearer')

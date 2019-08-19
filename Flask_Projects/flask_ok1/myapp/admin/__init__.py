#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint
import os

# 蓝图
admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')
# print(admin.template_folder)
# t = os.path.abspath(admin.template_folder)
# s = os.path.abspath(admin.static_folder)
# print(t)
# print(s)

from . import views

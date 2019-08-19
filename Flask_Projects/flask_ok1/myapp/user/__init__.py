#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint

print('user/init')

# 蓝图
user = Blueprint('user', __name__)

from . import views

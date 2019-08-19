# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 上午9:30
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : __init__.py.py
# @Software: PyCharm

from .views import bp
from utils.apiResult import api_result, CustomException
from werkzeug.exceptions import HTTPException
import traceback
from flask import request


@bp.app_errorhandler(Exception)
def errors(e):
    if isinstance(e, HTTPException) and (300 <= e.code < 600):
        print('-----HTTPException-----')
        traceback.print_exc()
        return api_result(code=e.code, message=str(e), data=request.method + ' ' + request.path)
    if isinstance(e, CustomException):
        print('-----CustomException-----')
        enums = e.err
        traceback.print_exc()
        # request.method + ' ' + request.path
        return api_result(code=enums._value_[0], message=enums._value_[1], data=request.method + ' ' + request.path)
    else:
        print('-----Exception-----')
        traceback.print_exc()
        return api_result(code=500, message=str(e), data=request.method + ' ' + request.path)

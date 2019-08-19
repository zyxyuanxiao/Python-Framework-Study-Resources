# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 下午11:44
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : views.py
# @Software: PyCharm

from flask import Blueprint, jsonify

bp = Blueprint('cms', __name__)


def api_result(code=None, message=None, data=None, details=None, status=None):
    result = {
        "code": code,
        "message": message,
        "data": data
    }

    if not result['data']:
        result.pop('data')
        return jsonify(result)
    return jsonify(result)


@bp.route('/')
def h():
    data = {
        "1": "a",
        "2": "b",
        "3": "c",
    }
    return api_result(code=200, message='okc', data=data)

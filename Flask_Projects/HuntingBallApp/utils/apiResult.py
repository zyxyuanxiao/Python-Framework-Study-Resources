# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 下午2:25
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : apiResult.py
# @Software: PyCharm

from flask import jsonify, abort
import flask_restful
from utils.customException import *


# 修改flask_restful.abort
def custom_abord(http_status_code, *args, **kwargs):
    if http_status_code == 400:
        abort(ab_enum(BaseEnum.Bad_Request))
    if http_status_code == 401:
        abort(ab_enum(BaseEnum.NOT_AUTHORIZED))
    if http_status_code == 403:
        abort(ab_enum(BaseEnum.FORBIDDEN))
    if http_status_code == 500:
        abort(ab_enum(BaseEnum.ServerError))
    if http_status_code == 666:
        abort(ab_enum(UserEnum.not_token))
    if http_status_code == 999:
        abort(ab_enum(UserEnum.already_regist))
    if http_status_code == 1000:
        abort(ab_enum(UserEnum.tel_length_err))
    if http_status_code == 1001:
        abort(ab_enum(UserEnum.not_tel))
    if http_status_code == 1002:
        abort(ab_enum(UserEnum.psw_length_err))
    if http_status_code == 1003:
        abort(ab_enum(UserEnum.psw_err))
    if http_status_code == 1004:
        abort(ab_enum(UserEnum.psw2_err))
    if http_status_code == 1066:
        abort(ab_enum(UserEnum.database_err))
    if http_status_code == 1005:
        abort(ab_enum(MatchEnum.in_non))
    if http_status_code == 1006:
        abort(ab_enum(ArticleEnum.not_article))
    return abort(http_status_code)


# 重写
flask_restful.abort = custom_abord


# 简化 flask_restful.abort
def error_abort(code):
    flask_restful.abort(code)


# 返回格式
def api_result(code=None, message=None, data=None, details=None, status=None):
    result = {
        "code": code,
        "message": message,
        "data": data,
    }

    if not result['data']:
        result.pop('data')
        return jsonify(result)
    return jsonify(result)

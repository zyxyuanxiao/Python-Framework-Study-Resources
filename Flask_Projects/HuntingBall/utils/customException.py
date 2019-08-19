# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 上午11:48
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : customException.py
# @Software: PyCharm

from enum import Enum


# 自定义异常接收枚举
class CustomException(Exception):
    err = None

    def __init__(self, err):
        self.err = err


class BaseEnum(Enum):
    Bad_Request = (400, '参数类型错误')
    NOT_AUTHORIZED = (401, '未登录-认证信息失败-令牌过期')
    FORBIDDEN = (403, '无权限')
    ServerError = (500, '服务器内部异常')


# 自定义异常枚举
class UserEnum(Enum):
    not_token = (666, '没token玩个毛')
    already_regist = (999, '手机号已注册')
    tel_length_err = (1000, '手机号应为11位')
    not_tel = (1001, '手机号未注册')
    psw_length_err = (1002, '密码少于6位')
    psw_err = (1003, '密码错误')
    psw2_err = (1004, '2次密码不一致')
    database_err = (1066, '数据库异常')


class MatchEnum(Enum):
    in_none = (1005, '信息不能为空')


class ArticleEnum(Enum):
    not_article = (1006, '未找到该文章')


def ab_enum(data):
    from flask import request, jsonify
    code = data._value_[0]
    msg = data._value_[1]
    req = request.method + ' ' + request.path
    r = {
        "code": code,
        "msg": msg,
        "request": req
    }
    return jsonify(r)

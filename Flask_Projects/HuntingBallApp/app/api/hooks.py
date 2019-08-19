# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 下午6:05
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : hooks.py
# @Software: PyCharm

from flask import g, request
from app.api.api_bp import bp
from app.api.userApi.models import Gambler
from config.config import *
from utils.apiResult import error_abort
from config.config import app_conf


@bp.before_request
def app_before_request():
    # if config.APP_USER_ID in session:
    #     user_id = session.get(config.APP_USER_ID)
    print(request.path)
    print(request.url)
    print(request.method)
    print(request.full_path)
    print('666', '测试编码')
    # Access-Control-Allow-origin
    is_token = 'Token' in dict(request.headers.to_list())  # 是否存在token

    if request.method == 'OPTIONS':
        return None

    if not is_token:
        error_abort(666)
    elif is_token:
        # token = request.headers["token"]
        token = request.headers.get('token')
        print('token', token, type(token), len(token))

        if token == 'null':  # token == ''
            g.app_user = None
            return None
        # if request.path == '/api/login/' and request.method == 'POST':  # 手动登录跳过
        #     return None
        get_user(token)  # 传入-有效token或过期token查找user

    else:
        g.app_user = None  # 防止找不app_user报错


def get_user(token):
    # tel = config.r.get('token:{}'.format(token))  # 通过token获取手机号
    if app_conf() == 'development':
        r = config_obj['development'].R  # redis实例
        print('dev-redis')
    else:
        r = config_obj['production'].R
        print('prod-redis')
    tel = r.get('token:{}'.format(token))
    # print('tel', tel)
    if not tel:  # token错误或者失效
        # print('token:错误没有找到对应的user')
        g.app_user = None
        error_abort(401)
    user_id = r.get(tel)  # 通过手机号获取用户id
    user = Gambler.query.get(user_id)  # 获取用户对象
    g.app_user = user  # 创建全局对象

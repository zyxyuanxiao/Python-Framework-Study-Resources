# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 下午3:56
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : hooks.py
# @Software: PyCharm

from flask import g, request
from .views import bp
from app.api.user.models import Gambler
import config
from utils.apiResult import ex_er


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
        ex_er(666)
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
    tel = config.r.get('token:{}'.format(token))  # 通过token获取手机号
    # print('tel', tel)
    if not tel:  # token错误或者失效
        # print('token:错误没有找到对应的user')
        g.app_user = None
        ex_er(401)
    user_id = config.r.get(tel)  # 通过手机号获取用户id
    user = Gambler.query.get(user_id)  # 获取用户对象
    g.app_user = user  # 创建全局对象

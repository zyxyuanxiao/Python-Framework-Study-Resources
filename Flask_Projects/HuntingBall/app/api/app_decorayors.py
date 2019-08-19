# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 下午4:53
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : app_decorayors.py
# @Software: PyCharm


from flask import session, g
from functools import wraps
from utils.apiResult import api_result
import config


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if config.APP_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return api_result(code='401', message='未登录')

    return inner


def check_vip(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if hasattr(g, 'app_user'):
            print('yes')
            print(g.app_user)
            if hasattr(g.app_user, 'level'):
                print('level', g.app_user.level)
                if g.app_user.level == '1':
                    return func(*args, **kwargs)
                else:
                    return api_result(code=403, message='非会员用户')
            else:
                return api_result(code='444', message='未登录')
        else:
            return api_result(code='401', message='登录失效～重新登录')

    return inner


def t(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('dddddddd')
        return func(*args, **kwargs)

    return inner


if __name__ == '__main__':
    print(r.get('token:764e2bc6176536bcb827ad3c313a049e'))
    print(r.hget('user:15013038819', 'token'))

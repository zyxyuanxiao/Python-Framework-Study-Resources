# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 下午4:57
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : tokens.py
# @Software: PyCharm

from flask import session, request, current_app
from utils.apiResult import api_result
import uuid
import hashlib
import time
import redis
from config.config import config_obj, app_conf

pool = config_obj[app_conf()].POOL
r = redis.Redis(connection_pool=pool)


# 生成token
def c_token(tel, password):
    m = hashlib.md5()
    # print(m)
    m.update(tel.encode(encoding="utf-8"))
    m.update(password.encode(encoding="utf-8"))
    m.update(str(int(time.time())).encode(encoding="utf-8"))
    token = m.hexdigest()
    # print(token)
    return token


# 存入token
def set_token(token, user):
    r.hmset('user:%s' % user.tel, {'token': token})
    r.set('token:%s' % token, user.tel)
    r.expire('user:%s' % user.tel, 3600 * 24 * 30)
    r.expire('token:%s' % token, 3600 * 24 * 30)

    # tk = str(uuid.uuid1())
    # r.set('login-' + tel, tk, ex=3600 * 24 * 30)
    # r.set('login-' + tel, tk, ex=30)


# 校验token
def check_token(user_obj, tel, password):
    k = 'user:{}'.format(tel)  # user:15013038819
    t = r.hget(k, 'token')  # c7cd6ce80fc3e9e53ca688502f185c14
    if r.hget(k, 'token'):
        r.delete('token:{}'.format(t))
        r.delete(tel)
        r.delete(k, 'token')
        # print('删除旧token')

    tk = c_token(tel, password)  # 生成token
    # print(tk)
    set_token(tk, user_obj)  # 生成redis文件夹形式的键值对
    r.set(tel, user_obj.id, 3600 * 24 * 30)  # 手机:id
    return tk


if __name__ == '__main__':
    # from app import create_app
    # from time import sleep
    #
    # app = create_app()
    # with app.test_request_context():
    #     u = Gambler.query.filter_by(id='FH3B9QoJ472Nds468QKpjJ').first()
    #     u2 = Gambler.query.filter_by(id='ZYqREwkkpDaDGxcSk2pH9X').first()
    #     print(u)
    #     print(u2)
    #
    # t = c_token('yyx', '123')
    # set_token(t, u)
    #
    # sleep(5)
    # t2 = c_token('yyx', '123')
    # set_token(t2, u2)

    """
    FLUSHDB 清除一个数据库,
    FLUSHALL清除整个redis数据。
    """

    # x = '7bcc75802639d191df495d29c118dfe8'
    # t = '15013038819'
    # t2 = 'user:{}'.format(t)
    # print(t2)
    # print(r.get('token:{}'.format(x)))
    # print(r.hget(t2, 'token'))

    'https://python3-cookbook.readthedocs.io/zh_CN/latest/index.html'

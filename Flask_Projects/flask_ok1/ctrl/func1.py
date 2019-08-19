#!/usr/bin/env python
# encoding: utf-8

import hashlib
import random
from functools import wraps
from flask import make_response, jsonify

import redis

# host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)


# r = redis.Redis(host='localhost', port=6379,db=0)

def md5(s):
    m = hashlib.md5()
    m.update(s.encode(encoding="utf-8"))
    return m.hexdigest()


def rd():
    r = random.randint(1000, 9999)
    print(r)
    return r


# 跨域
def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst

    return wrapper_fun

# def login_check(f):
#     @wraps(f)
#     def decorator(*args, **kwargs):
#         token = request.headers.get('token')
#         if not token:
#             return jsonify({'code': 0, 'message': '需要验证'})
#
#         mobile = r.get('token:%s' % token)
#         if not mobile or token != r.hget('user:%s' % mobile, 'token'):
#             return jsonify({'code': 2, 'message': '验证信息错误'})
#
#         return f(*args, **kwargs)
#
#     return decorator

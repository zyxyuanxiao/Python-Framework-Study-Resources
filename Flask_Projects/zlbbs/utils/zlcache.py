# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 下午5:44
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : zlcache.py
# @Software: PyCharm

from redis import Redis

r = Redis(host='127.0.0.1', port=6379, password=123456)


def set(key, value, timeout=60):
    return r.set(key, value, timeout)


def get(key):
    return r.get(key)


def delete(key):
    return r.delete(key)

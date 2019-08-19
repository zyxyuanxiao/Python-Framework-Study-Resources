# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 上午9:36
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : config.py
# @Software: PyCharm

import redis
from datetime import timedelta

# SECRET_KEY = os.urandom(24)
SECRET_KEY = 'ShaHeTop-Almighty-ares'  # session加密
PERMANENT_SESSION_LIFETIME = timedelta(days=30)  # 设置session过期时间
CMS_USER_ID = 'cms'
APP_USER_ID = 'user'
APP_USER_TOKEN = 'user token'

# DEBUG = True
DEBUG = False
host = '0.0.0.0'
# port = 9999
port = 5000

"""Mysql"""
HOSTNAME = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
# PASSWORD = '123456'
PASSWORD = 'okcokc111111'
DATABASE = 'HuntingBall'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

"""Redis"""
# host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
# redis_pwd = 123456
redis_pwd = 'okc1111'
pool = redis.ConnectionPool(host='localhost', port=6379, password=redis_pwd, decode_responses=True, db=1)
r = redis.Redis(connection_pool=pool)






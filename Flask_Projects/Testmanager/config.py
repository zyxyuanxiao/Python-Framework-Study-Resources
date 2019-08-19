# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 上午9:38
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : config.py
# @Software: PyCharm

import os


class Config(object):
    debug = True
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)

    # mysql数据库
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    USERNAME = 'root'
    PASSWORD = '123456'
    DATABASE = 'testmanager'
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
    # app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True

#!/usr/bin/env python
# encoding: utf-8
import os

# 正式服:
#       1.调试,
#       2.数据库密码
#       3.run.py 文件
#       4.module.py 文件
#       5.图片路径

# 调试
DEBUG = True
# DEBUG = False

# session加密
SECRET_KEY = os.urandom(24)

# mysql数据库
HOSTNAME = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
# PASSWORD = 'OKCokc6666'
PASSWORD = '123456'
DATABASE = 'okc'

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

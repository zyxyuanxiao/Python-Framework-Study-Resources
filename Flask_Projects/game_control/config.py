#!/usr/bin/env python
# encoding: utf-8
import os
from datetime import timedelta


#       1.环境:__init__
#       2.run.py 文件
#       3.图片路径

# 基本配置类
class BaseConfig:
    # session加密
    SECRET_KEY = os.urandom(24)
    # 设置session过期时间
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)


# 开发环境
class DevelopmentConfig(BaseConfig):
    # 调试
    DEBUG = True
    # mysql数据库
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    USERNAME = 'root'
    PASSWORD = '123456'
    DATABASE = 'game'
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True


# 生产环境
class ProductionConfig(BaseConfig):
    # 调试
    DEBUG = False
    # mysql数据库
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    USERNAME = 'root'
    PASSWORD = 'OKCokc6666'
    DATABASE = 'game'
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config = {
    'development': DevelopmentConfig,
    'productionConfig': ProductionConfig,
    'default': DevelopmentConfig,

}

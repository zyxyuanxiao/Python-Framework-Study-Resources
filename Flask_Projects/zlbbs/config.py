# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 上午9:31
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : config.py
# @Software: PyCharm
import os

DEBUG = True
# SECRET_KEY = os.urandom(24)
SECRET_KEY = 'yyyyyyyyyyyyyyy'
CMS_USER_ID = 'cms'
FRONT_USER_ID = 'front'

# 邮件
# MAIL_USE_TLS：端口号587
# MAIL_USE_SSL：端口号465
# QQ邮箱不支持非加密方式发送邮件
# 发送者邮箱的服务器地址
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL : default False
MAIL_USERNAME = '872540033@qq.com'
MAIL_PASSWORD = 'wjuodrdsajqnbbia'
MAIL_DEFAULT_SENDER = '872540033@qq.com'

# mysql数据库
HOSTNAME = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = 'flask_project'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 阿里大于相关配置
ALIDAYU_APP_KEY = '23709557'
ALIDAYU_APP_SECRET = 'd9e430e0a96e21c92adacb522a905c4b'
ALIDAYU_SIGN_NAME = '小饭桌应用'
ALIDAYU_TEMPLATE_CODE = 'SMS_68465012'

# UEditor的相关配置
UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = "M4zCEW4f9XPanbMN-Lb9O0S8j893f0e1ezAohFVL"
UEDITOR_QINIU_SECRET_KEY = "7BKV7HeEKM3NDJk8_l_C89JI3SMmeUlAIatzl9d4"
UEDITOR_QINIU_BUCKET_NAME = "hyvideo"
UEDITOR_QINIU_DOMAIN = "http://7xqenu.com1.z0.glb.clouddn.com/"

# flask-paginate的相关配置
PER_PAGE = 10

# celery相关的配置
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"

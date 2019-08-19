#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from config import config
from exts import db
from flask_cors import CORS

# from datetime import timedelta

print('client/init')
# 创建项目对象

app = Flask(__name__)

CORS(app, supports_credentials=True)

# 指向配置地址
# 获取相应的配置类
app.config.from_object(config['default'])
# app.config.from_object(config['productionConfig'])

# 初始化／创建数据库对象
db.init_app(app)

# 设置session过期时间
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)

# flask-login
# app.secret_key = 'yang'
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'lien'
login_manager.login_message = '请登录!'
login_manager.init_app(app)

# 图片
# 上传集，这是这个插件的基础，相当于上传文件的集合
photos = UploadSet('photos', IMAGES)

# 上传文件存储位置
UPLOAD_FOLDER = '/Users/yangyuexiong/Desktop/images'
# UPLOAD_FOLDER = '/root/images'
app.config['UPLOADED_PHOTOS_DEST'] = UPLOAD_FOLDER

# 设置允许存储的类型,DOCUMENTS是预设的类型集合
app.config['UPLOADED_DOC_ALLOW'] = IMAGES

# 绑定app
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

from app import views, models

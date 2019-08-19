#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import config
from exts import db
from datetime import timedelta

print('myapp/init')
# 创建项目对象

app = Flask(__name__)

# 跨域
CORS(app, supports_credentials=True)

# 指向配置地址
app.config.from_object(config)

# 初始化／创建数据库对象
db.init_app(app)

# 设置session过期时间
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)

# flask-login
app.secret_key = 'yang'
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'admin.login'
login_manager.login_message = '请登录!'
login_manager.init_app(app)

# 图片
# 上传集，这是这个插件的基础，相当于上传文件的集合
photos = UploadSet('photos', IMAGES)
# print(photos)
# 上传文件存储位置
UPLOAD_FOLDER = '/Users/yangyuexiong/Desktop/images'
# UPLOAD_FOLDER = '/root/images'
app.config['UPLOADED_PHOTOS_DEST'] = UPLOAD_FOLDER
# print(UPLOAD_FOLDER)
# print(os.getcwd())  # 默认路径

# 设置允许存储的类型,DOCUMENTS是预设的类型集合
app.config['UPLOADED_DOC_ALLOW'] = IMAGES
# print(app.config['UPLOADED_DOC_ALLOW'])

# 绑定app
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

# 蓝图注册
from .user import user as user_blueprint

app.register_blueprint(user_blueprint, url_prefix='/user')

from .admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint, url_prefix='/admin')

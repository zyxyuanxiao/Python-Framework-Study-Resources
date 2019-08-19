# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 上午9:28
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from flask_cors import CORS, cross_origin
import config
from exts import db
from app.api import bp as api_bp, api
from app.cms import bp as cms_bp
from app.common import bp as common_bp
from utils.apiResult import ex_er
from datetime import date


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        else:
            ex_er(500)


class Flask(_Flask):
    json_encoder = JSONEncoder


def create_app():
    app = Flask(__name__)  # 实例
    CORS(app, supports_credentials=True)  # 跨域
    app.config.from_object(config)  # 配置
    app.register_blueprint(api_bp)  # register Api
    app.register_blueprint(cms_bp)  # register CMS
    app.register_blueprint(common_bp)  # register Common
    db.init_app(app)  # 初始化db
    return app

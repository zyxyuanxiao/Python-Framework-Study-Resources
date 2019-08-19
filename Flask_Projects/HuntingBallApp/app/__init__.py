# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 下午3:54
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from extend_libs.exts import db
from utils.apiResult import error_abort
from flask_cors import CORS


class JSONEncoder(_JSONEncoder):
    """重写flask序列化"""

    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        from datetime import date
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        else:
            error_abort(500)


class Flask(_Flask):
    """重写注册"""

    json_encoder = JSONEncoder


def register_bp(app):
    """蓝图注册"""

    from app.cms.admin import bp as cms_bp
    from app.api import bp as api_bp
    app.register_blueprint(cms_bp, url_prefix='/v1/cms')
    app.register_blueprint(api_bp, url_prefix='/v1/api')


def register_config(app):
    """配置文件"""

    from config.config import config_obj, app_conf
    app.config.from_object(config_obj[app_conf()])  # 环境配置
    config_obj[app_conf()].init_app(app)


def create_app():
    app = Flask(__name__)  # 实例
    CORS(app, supports_credentials=True)  # 跨域
    register_config(app)
    register_bp(app)
    db.init_app(app)  # db初始化
    return app

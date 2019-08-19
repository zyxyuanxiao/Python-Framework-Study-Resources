# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 上午9:35
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : __init__.py.py
# @Software: PyCharm

# from flask import Flask
# from apps.cms import bp as cms_bp
# from apps.front import bp as front_bp
# from apps.common import bp as common_bp
# import config
# from exts import db, mail
# from flask_wtf import CSRFProtect
#
#
# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(config)
#
#     app.register_blueprint(cms_bp)
#     app.register_blueprint(front_bp)
#     app.register_blueprint(common_bp)
#
#     db.init_app(app)
#     mail.init_app(app)
#     CSRFProtect(app)
#     return app

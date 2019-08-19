# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 下午3:54
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : __init__.py.py
# @Software: PyCharm

from . import hooks
from flask_restful import Api, Resource
from .userApi.views import UserRegisterApi, UserLoginApi
from .api_bp import bp

api = Api(bp)
api.add_resource(UserRegisterApi, '/register', '/register/<user_id>', endpoint='register')
api.add_resource(UserLoginApi, '/login', '/login/<user_id>/<token>', endpoint='login')

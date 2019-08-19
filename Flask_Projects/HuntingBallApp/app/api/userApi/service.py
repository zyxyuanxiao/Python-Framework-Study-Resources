# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 下午2:15
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : service.py
# @Software: PyCharm


from flask import g, request
from flask_restful import reqparse
from app.api.userApi.models import Gambler
import threading
from utils.apiResult import error_abort
from utils.tokens import check_token
from extend_libs.exts import db
import datetime

now_time = datetime.datetime.now()


class UserRegisterService:
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(UserRegisterService, '_instance'):
            with UserRegisterService._instance_lock:
                if not hasattr(UserRegisterService, '_instance'):
                    UserRegisterService._instance = object.__new__(cls)
        return UserRegisterService._instance

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('tel', type=int, required=True, trim=True, location='json')
        self.reqparse.add_argument('password', type=str, required=True, trim=True, location='json')
        self.reqparse.add_argument('password2', type=str, required=True, trim=True, location='json')
        # super(UserRegisterService, self).__init__()

    def register(self):
        args = self.reqparse.parse_args()
        print(args)
        u = Gambler.query.filter_by(tel=args["tel"]).first()
        if u:
            error_abort(999)
        if len(str(args["tel"])) != 11:
            error_abort(1000)
        if len(args["password"]) < 6:
            error_abort(1002)
        if args["password"] != args["password2"]:
            error_abort(1004)
        return args


class UserLoginService:
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(UserLoginService, '_instance'):
            with UserLoginService._instance_lock:
                if not hasattr(UserLoginService, '_instance'):
                    UserLoginService._instance = object.__new__(cls)
        return UserLoginService._instance

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('tel', type=int, required=True, trim=True, location='json')
        self.reqparse.add_argument('password', type=str, required=True, trim=True, location='json')
        super(UserLoginService, self).__init__()

    def login(self):
        args = self.reqparse.parse_args()
        u = Gambler.query.filter_by(tel=args["tel"]).first()
        if len(str(args["tel"])) != 11:
            error_abort(1000)
        if not u:
            error_abort(1001)
        if len(args["password"]) < 6:
            error_abort(1002)
        if not u.check_password(args["password"]):
            error_abort(1003)
        if u and u.check_password(args["password"]):
            # session[config.APP_USER_ID] = u.id
            # session.permanent = True
            if not g.app_user:
                tk = check_token(u, u.tel, args["password"])

                with db.auto_commit():
                    u.join_time = now_time
                    print('%s:更新登录时间' % u)
                g.app_user = u
                return u, True, tk
            else:
                with db.auto_commit():
                    u.join_time = now_time
                    print('%s:更新登录时间' % u)
                tk = request.headers.get('token')
                return u, True, tk
        return args

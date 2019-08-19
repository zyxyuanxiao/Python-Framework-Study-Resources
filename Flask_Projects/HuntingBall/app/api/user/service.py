# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 下午4:03
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : service.py
# @Software: PyCharm

from flask import g
from flask_restful import reqparse
from app.api.user.models import Gambler
import threading
from utils.apiResult import ex_er
from utils.tokens import check_token


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
        super(UserRegisterService, self).__init__()

    def register(self):
        args = self.reqparse.parse_args()
        u = Gambler.query.filter_by(username=args["tel"]).first()
        if u:
            ex_er(999)
        if len(str(args["tel"])) != 11:
            ex_er(1000)
        if len(args["password"]) < 6:
            ex_er(1002)
        if args["password"] != args["password2"]:
            ex_er(1004)
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
        u = Gambler.query.filter_by(username=args["tel"]).first()
        if len(str(args["tel"])) != 11:
            ex_er(1000)
        if not u:
            ex_er(1001)
        if len(args["password"]) < 6:
            ex_er(1002)
        if not u.check_passwodr(args["password"]):
            ex_er(1003)
        if u and u.check_passwodr(args["password"]):
            # session[config.APP_USER_ID] = u.id
            # session.permanent = True
            if not g.app_user:
                tk = check_token(u, u.username, args["password"])

                import datetime
                now_time = datetime.datetime.now()
                u.join_time = now_time
                from exts import db
                db.session.commit()
                g.app_user = u
                return u, True, tk
            else:
                from flask import request
                tk = request.headers.get('token')
                return u, True, tk
        return args


if __name__ == '__main__':
    x1 = UserRegisterService()
    x = UserRegisterService()
    y = UserLoginService()
    y2 = UserLoginService()
    print(x)
    print(x1)
    print(y)
    print(y2)

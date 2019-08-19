# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 上午9:39
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : views.py
# @Software: PyCharm

from flask_restful import Resource, marshal_with, fields
from flask import request, g, redirect, url_for
from utils.apiResult import api_result, ex_er
from app.api.user.models import Gambler
from app.api.user.service import UserRegisterService, UserLoginService
from app.api.user.repository import UserModel
import config
from utils.tokens import check_token
from app.api.app_decorayors import t


class UserRegisterApi(Resource):
    user_fields = {
        'user_id': fields.String(attribute='id'),
        'username': fields.String,
        'nickname': fields.String,
        'level': fields.String,
        'money': fields.String(default='9999999999999999'),
    }

    @marshal_with(user_fields, envelope='data')
    def get(self, user_id):
        u = Gambler.query.filter_by(id=user_id).first()
        return u, 200

    def post(self):
        # data = request.get_json()
        args = UserRegisterService().register()
        tel = args['tel']
        password = args['password']
        u = UserModel(tel, password).user_register()  # 注册成功
        tk = check_token(u, u.username, password)  # 生成token
        g.app_user = u
        return redirect(url_for('api.login', user_id=u.id, token=tk))  # 自动登录


class UserLoginApi(Resource):

    def get(self, user_id, token):
        u = Gambler.query.filter_by(id=user_id).first()
        t = config.r.get('token:{}'.format(token))
        if u and int(u.username) == int(t):  # mysql中手机号对比token查出的手机号是否一致
            u['token'] = token
            g.app_user = u
            return api_result(code=200, message='注册并登录成功', data=u)
        else:
            ex_er(401)

    def post(self):
        self.data = request.get_json()
        # print(self.data)
        # tel = request.json.get('tel')
        # print(tel)
        args = UserLoginService().login()
        # print(args)
        if args:
            tk = args[2]
            user = dict(args[0])
            user['token'] = tk
            return api_result(code=200, message='登录成功', data=user)
        return api_result(code=500, message='服务器异常')

    def put(self):
        pass

    def delete(self):
        # session.clear()
        if g.app_user:
            k = 'user:{}'.format(g.app_user.username)  # user:15013038819
            t = config.r.hget(k, 'token')  # c7cd6ce80fc3e9e53ca688502f185c14
            # print(k, t)
            config.r.delete('token:{}'.format(t))
            config.r.delete(g.app_user.username)
            config.r.delete(k, 'token')

            import datetime
            now_time = datetime.datetime.now()
            g.app_user.logout_time = now_time
            from exts import db
            db.session.commit()
        else:
            return api_result(code=505, message='用户不存在或已退出')
        return api_result(code=200, message='退出成功')


class Test(Resource):
    decorators = [t]

    def get(self):
        u = Gambler.query.filter_by(id='YfpgoLZtEGPfMXUvFPffCi').first()
        return api_result(code=200, message='', data=u)

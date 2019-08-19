# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 下午1:44
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : views.py
# @Software: PyCharm

from flask_restful import Resource, marshal_with, fields
from flask import request, g
from app.api.userApi.service import UserRegisterService, UserLoginService
from app.api.userApi.repository import UserModel
from app.api.userApi.models import Gambler
from utils.apiResult import api_result, error_abort


class UserRegisterApi(Resource):
    user_fields = {
        'user_id': fields.String(attribute='id'),
        'tel': fields.String,
        'nickname': fields.String,
        'level': fields.String,
        'money': fields.String(default='9999999999999999'),
    }

    @marshal_with(user_fields, envelope='data')
    def get(self, user_id):
        u = Gambler.query.filter_by(id=user_id).first()
        return u, 200

    def post(self):
        data = request.get_json()
        # data = request.json
        print(data)

        args = UserRegisterService().register()
        print(args)
        u = UserModel(tel=args['tel'], password=args['password']).user_register()  # 注册成功
        # tk = check_token(u, u.tel, password)  # 生成token
        # g.app_user = u
        # return redirect(url_for('api.login', user_id=u.id, token=tk))  # 自动登录
        return api_result(code=200, message='ok', data=u)

    def delete(self, user_id):
        u = Gambler.query.filter_by(id=user_id).first()
        print(u)
        from extend_libs.exts import db
        with db.auto_commit():
            u.delete()


class UserLoginApi(Resource):

    def get(self, user_id, token):
        u = Gambler.query.filter_by(id=user_id).first()
        t = config.r.get('token:{}'.format(token))
        if u and int(u.username) == int(t):  # mysql中手机号对比token查出的手机号是否一致
            u['token'] = token
            g.app_user = u
            return api_result(code=200, message='注册并登录成功', data=u)
        else:
            error_abort(401)

    def post(self):
        # from validators.user_vali import LoginForm
        # data = request.get_json()
        # print(data)
        # form = LoginForm()
        # print(form.tel)
        # print(form.password)
        # print(form.validate())
        # if form.validate():
        #     print('1')
        #     return api_result(code=200, message='okc')
        # print(form.errors)
        # return api_result(message=form.errors)
        """—————— ——————"""
        args = UserLoginService().login()
        print(args)
        try:
            tk = args[2]
            user = dict(args[0])
            user['token'] = tk
            return api_result(code=200, message='登录成功', data=user)
        except BaseException as e:
            print(e)
            error_abort(500)

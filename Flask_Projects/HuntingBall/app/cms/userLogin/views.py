# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 上午10:36
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : views.py
# @Software: PyCharm

from flask import views, request, session
from .models import CMSUser
from .cms_decorators import login_required
from utils.apiResult import api_result
import config
from app.cms.views import bp


@bp.route('/logout')
@login_required
def logout():
    session.clear()
    return api_result(code=200, message='退出成功')


class LoginView(views.MethodView):
    def get(self):
        return 'this login view'

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        checkout = request.form.get('check_out')
        # print(username, password)
        admin = CMSUser.query.filter_by(username=username).first()
        # print(admin)
        # print(type(admin))
        # print(type(admin.username))
        p = admin.check_password(password)
        # print(p)

        if not admin:
            return api_result(code=200, message='该admin不存在', data=None)

        if not p:
            return api_result(code=200, message='密码错误', data=None)
        else:
            session[config.CMS_USER_ID] = admin.id
            session.permanent = True
            # print('id:', session[config.CMS_USER_ID])
            if checkout:
                session.permanent = True
            return api_result(code=200, message='登录成功', data={
                'admin': admin.username,
                'permissions': admin.permissions
            })

# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 上午11:23
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : repository.py
# @Software: PyCharm


from app.api.userApi.models import Gambler
from extend_libs.exts import db
import threading
from flask import abort


class UserModel(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(UserModel, '_instance'):
            with UserModel._instance_lock:
                if not hasattr(UserModel, '_instance'):
                    UserModel._instance = object.__new__(cls)
        return UserModel._instance

    def __init__(self, tel, password):
        self.tel = tel
        self.password = password

    def user_register(self):
        u = Gambler(self.tel, self.password)
        try:
            with db.auto_commit():
                db.session.add(u)
        except BaseException as e:
            import traceback
            traceback.print_exc()
            print('数据库异常:%s' % e)
            abort(500)
        return u

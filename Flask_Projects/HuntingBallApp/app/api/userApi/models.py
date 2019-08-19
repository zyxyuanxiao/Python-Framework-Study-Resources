# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 下午1:44
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : models.py
# @Software: PyCharm


from extend_libs.exts import db, Base
from werkzeug.security import generate_password_hash, check_password_hash
import shortuuid


class Gambler(Base):
    __tablename__ = 'gambler'
    id = db.Column(db.String(128), primary_key=True, default=shortuuid.uuid, index=True)
    tel = db.Column(db.String(64), unique=True, nullable=False)
    _password = db.Column(db.String(256), nullable=False)
    nickname = db.Column(db.String(128), default='普通用户')
    level = db.Column(db.String(64), default='1')
    register_time = db.Column(db.DateTime, server_default=db.func.now())
    join_time = db.Column(db.String(128), server_default='')
    logout_time = db.Column(db.String(128), server_default='')

    def __init__(self, tel, password):
        self.tel = tel
        self.password = password
        self.nickname = '普通用户'
        self.level = '1'

    def keys(self):
        model_list = ['id', 'tel', 'nickname', 'level']
        return model_list

    def __repr__(self):
        return 'User: <id:%s tel:%s nk:%s lv:%s >' % (
            self.id,
            self.tel,
            self.nickname,
            self.level)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, newpwd):
        self._password = generate_password_hash(newpwd)

    def check_password(self, raw_password):
        # args1:经过加密的密码
        # args2:原生密码
        # print('args1', type(self.password))
        # print('args2', raw_password)
        resule = check_password_hash(self.password, raw_password)
        return resule

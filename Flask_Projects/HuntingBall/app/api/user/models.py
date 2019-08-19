# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 上午9:39
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : models.py
# @Software: PyCharm

from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import shortuuid


class Gambler(db.Model):
    __tablename__ = 'gambler'
    id = db.Column(db.String(128), primary_key=True, default=shortuuid.uuid, index=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    _password = db.Column(db.String(256), nullable=False)
    nickname = db.Column(db.String(128), default='普通用户')
    level = db.Column(db.String(64), default='1')
    register_time = db.Column(db.DateTime, server_default=db.func.now())
    join_time = db.Column(db.String(128), server_default='')
    logout_time = db.Column(db.String(128), server_default='')

    def __init__(self, username, password, nickname='普通用户', level='1'):
        self.username = username
        self.password = password
        self.nickname = nickname
        self.level = level

    def __repr__(self):
        return 'User: <id:%s tel:%s nk:%s lv:%s >' % (
            self.id,
            self.username,
            self.nickname,
            self.level)

    def keys(self):
        return ['id', 'username', 'nickname', 'level']

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, newpwd):
        self._password = generate_password_hash(newpwd)

    def check_passwodr(self, raw_password):
        # args1:经过加密的密码
        # args2:原生密码
        resule = check_password_hash(self.password, raw_password)
        return resule

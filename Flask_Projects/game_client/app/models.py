#!/usr/bin/env python
# encoding: utf-8

from exts import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# app用户
class Gambler(db.Model, UserMixin):
    __tablename__ = 'gambler'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    nickname = db.Column(db.String(128), nullable=True)
    level = db.Column(db.String(64), default='1')
    register_time = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, username, password, nickname, level):

        self.username = username
        self.password = generate_password_hash(password)
        self.nickname = nickname
        self.level = level

    def check_passwodr(self, raw_password):
        resule = check_password_hash(self.password, raw_password)
        return resule

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<User: 用户名 %s 密码 %s %s %s >' % (
            self.username,
            self.password,
            self.nickname,
            self.level,
        )

    def is_admin(self):
        return False


# 登录时间
class Monitor(db.Model):
    __tablename__ = 'monitor'
    id = db.Column(db.Integer, primary_key=True)
    mobile = db.Column(db.String(64))
    login_t = db.Column(db.DateTime, server_default=db.func.now())
    logout_t = db.Column(db.DateTime)

    def __init__(self, mobile):
        self.mobile = mobile


# 比赛场次信息
class Match(db.Model):
    __tablename__ = 'match'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vs_type = db.Column(db.String(128), nullable=False)
    vs = db.Column(db.String(128), nullable=False)
    vs_code = db.Column(db.String(128), nullable=False)
    vs_time = db.Column(db.String(128), nullable=False)
    victory = db.Column(db.String(128), nullable=False)
    ping = db.Column(db.String(128), nullable=False)
    fail = db.Column(db.String(128), nullable=False)
    victory_code = db.Column(db.String(128), nullable=False)
    ping_code = db.Column(db.String(128), nullable=False)
    fail_code = db.Column(db.String(128), nullable=False)
    let_ball = db.Column(db.String(128), nullable=False)
    cea_time = db.Column(db.DateTime, server_default=db.func.now())


# 文章
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(128), nullable=False)
    vs_category = db.Column(db.String(128), nullable=False)
    vs_other_c = db.Column(db.String(128), nullable=True)
    vs = db.Column(db.String(128), nullable=False)
    al = db.Column(db.String(128), nullable=False)
    link = db.Column(db.String(128), nullable=True)
    content = db.Column(db.Text, nullable=False)
    vs_push = db.Column(db.String(128), nullable=True)
    state = db.Column(db.String(128), nullable=True)
    image_name = db.Column(db.String(128))
    image_path = db.Column(db.String(256))
    cea_time = db.Column(db.DateTime, server_default=db.func.now())


# 推荐的比赛
class Push(db.Model):
    __tablename__ = 'push'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vs = db.Column(db.String(128), nullable=False)
    victory = db.Column(db.String(128), nullable=False)
    ping = db.Column(db.String(128), nullable=False)
    fail = db.Column(db.String(128), nullable=False)
    victory_code = db.Column(db.String(128), nullable=False)
    ping_code = db.Column(db.String(128), nullable=False)
    fail_code = db.Column(db.String(128), nullable=False)
    let_ball = db.Column(db.String(128), nullable=False)
    pusher = db.Column(db.String(128), nullable=False)
    main_push = db.Column(db.String(128), nullable=False)
    cost = db.Column(db.String(64))
    describe = db.Column(db.Text)
    cea_time = db.Column(db.DateTime, server_default=db.func.now())


'''_______________________________后台表_____________________________________'''


# 管理后台用户
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=True)
    nickname = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(128), nullable=False)
    register_time = db.Column(db.DateTime, server_default=db.func.now())

    # mysql5.5
    # register_time = db.Column(db.TIMESTAMP, server_default=db.func.now())

    def __init__(self, *args, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        nickname = kwargs.get('nickname')
        address = kwargs.get('address')
        city = kwargs.get('city')
        country = kwargs.get('country')

        self.username = username
        self.password = generate_password_hash(password)
        self.nickname = nickname
        self.address = address
        self.city = city
        self.country = country

    def check_passwodr(self, raw_password):
        resule = check_password_hash(self.password, raw_password)
        return resule

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except NameError:
            return str(self.id)

    def is_admin(self):
        return True

    def __repr__(self):
        return '<User: 用户名 %s 密码 %s 昵称 %s 地区 %s 城市 %s 国家 %s >' % (
            self.username,
            self.password,
            self.nickname,
            self.address,
            self.city,
            self.country)


# 房子
class House(db.Model):
    __tablename__ = 'house'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    region = db.Column(db.String(64), nullable=False)
    price = db.Column(db.String(64), nullable=False)
    area = db.Column(db.String(64), nullable=True)
    households = db.Column(db.String(64), nullable=False)
    describe = db.Column(db.String(1024), nullable=True)

    image_name = db.Column(db.String(128))
    image_path = db.Column(db.String(256))

    auth_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('houses'))

    release_time = db.Column(db.DateTime, server_default=db.func.now())
    # release_time = db.Column(db.TIMESTAMP, server_default=db.func.now())

    # users = db.relationship('User', backref='role')
    # 添加到 Role 模型中的 users 属性代表这个关系的面向对象视角。
    # 对于一个 Role 类的实例,其 users 属性将返回与角色相关联的用户组成的列表。
    # db.relationship() 的第一个参数表,如果模型类尚未定义,可使用字符串形式指定。
    # db.relationship() 中的 backref 参数向 User 模型中添加一个 role 属性,从而定义反向关系。
    # 这一属性可替代 role_id 访问 Role 模型,此时获取的是模型对象


# app个人资料
class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nkname = db.Column(db.String(64), nullable=True, default='')
    tel = db.Column(db.String(64), default='')
    u_id = db.Column(db.Integer, db.ForeignKey('gambler.id'))
    u_Profile = db.relationship('Gambler', backref=db.backref('profiles'))


if __name__ == '__main__':
    pass

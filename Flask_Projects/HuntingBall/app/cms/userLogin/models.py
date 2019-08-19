# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 上午10:36
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : models.py
# @Software: PyCharm

from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.cms.article.models import Article


# 权限
class CMSPersmission(object):
    # 255的二进制方式来表示 1111 1111
    ALL_PERMISSION = 0b11111111
    # 1. 访问者权限
    VISITOR = 0b00000001
    # 2. 管理帖子权限
    POSTER = 0b00000010
    # 3. 管理评论的权限
    COMMENTER = 0b00000100
    # 4. 管理板块的权限
    BOARDER = 0b00001000
    # 5. 管理前台用户的权限
    FRONTUSER = 0b00010000
    # 6. 管理后台用户的权限
    CMSUSER = 0b00100000
    # 7. 管理后台管理员的权限
    ADMINER = 0b01000000


cms_role_user = db.Table(
    'cms_role_user',  # 表名
    # 字段名:cms_role_id,
    # 类型
    # 外键:cms_role.id,
    # 设置为主键
    db.Column('cms_role_id', db.Integer, db.ForeignKey('cms_role.id'), primary_key=True),
    db.Column('cms_user_id', db.Integer, db.ForeignKey('cms_user.id'), primary_key=True)
)


# CMS角色
class CMSRole(db.Model):
    __tablename__ = 'cms_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(200), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    permissions = db.Column(db.Integer, default=CMSPersmission.VISITOR)

    # 引用模型:CMSUser
    # 中间表:cms_role_user
    # 通过CMSUser反向引用:roles
    users = db.relationship('CMSUser', secondary=cms_role_user, backref='roles')


# CMS用户
class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    join_time = db.Column(db.DateTime, server_default=db.func.now())

    articles = db.relationship(Article, backref='user')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result

    @property
    def permissions(self):
        if not self.roles:
            return 0
        all_permissions = 0
        for role in self.roles:
            permissions = role.permissions
            all_permissions |= permissions  # 整合该用户所有权限
            # print('权限包含：', all_permissions)
        return all_permissions

    # 是否拥有权限
    def has_permission(self, permission):
        # all_permissions = self.permissions
        # result = all_permissions&permission == permission
        # return result
        return self.permissions & permission == permission

    # 开发者
    @property
    def is_developer(self):
        return self.has_permission(CMSPersmission.ALL_PERMISSION)

    def __repr__(self):
        return '<admin: 用户名 %s 密码 %s  >' % (
            self.username,
            self.password,
        )

# class Article(db.Model):
#     __tablename__ = 'article'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(128), nullable=False)
#     author = db.Column(db.String(128), nullable=False)
#     vs_category = db.Column(db.String(128), nullable=False)
#     vs_other_c = db.Column(db.String(128), nullable=True)
#     vs = db.Column(db.String(128), nullable=False)
#     al = db.Column(db.String(128), nullable=False)
#     link = db.Column(db.String(128), nullable=True)
#     content = db.Column(db.Text, nullable=False)
#     vs_push = db.Column(db.String(128), nullable=True)
#     state = db.Column(db.String(128), nullable=True)
#     image_name = db.Column(db.String(128))
#     image_path = db.Column(db.String(256))
#     a_status = db.Column(db.String(128), default='1')
#     watch = db.Column(db.String(128), default='999')
#     cea_time = db.Column(db.DateTime, server_default=db.func.now())
#
#     uid = db.Column(db.Integer, db.ForeignKey('cms_user.id'))
#
#     def __repr__(self):
#         return '<article: 文章[id:%s] 作者[id:%s]>' % (
#             self.id,
#             self.uid,
#         )

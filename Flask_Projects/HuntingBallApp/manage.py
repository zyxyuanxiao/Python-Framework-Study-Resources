# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 下午1:55
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : manage.py
# @Software: PyCharm


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from extend_libs.exts import db
from app.cms.admin import models as cms_models
from app.api.userApi.models import Gambler

app = create_app()
# 实例
manager = Manager(app)
# 绑定
Migrate(app, db)
# 添加命令
manager.add_command('db', MigrateCommand)

# CMS
CMSUser = cms_models.CMSUser
CMSRole = cms_models.CMSRole
CMSPermission = cms_models.CMSPersmission


# 创建CMS用户
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
def create_cms_user(username, password):
    user = CMSUser(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    print('CMS用户添加成功')


# CMS权限
@manager.command
def create_role():
    # 1. 访问者（可以修改个人信息）
    visitor = CMSRole(name='访问者', desc='只能相关数据，不能修改。')
    visitor.permissions = CMSPermission.VISITOR

    # 2. 运营角色（修改个人个人信息，管理帖子，管理评论，管理前台用户）
    operator = CMSRole(name='运营', desc='管理帖子，管理评论,管理前台用户。')
    operator.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.CMSUSER | CMSPermission.COMMENTER | CMSPermission.FRONTUSER

    # 3. 管理员（拥有绝大部分权限）
    admin = CMSRole(name='管理员', desc='拥有本系统所有权限。')
    admin.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.CMSUSER | CMSPermission.COMMENTER | CMSPermission.FRONTUSER | CMSPermission.BOARDER

    # 4. 开发者
    developer = CMSRole(name='开发者', desc='开发人员专用角色。11111')
    developer.permissions = CMSPermission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()
    print('角色创建完成')


# 赋予用户权限
@manager.option('-u', '--username', dest='username')
@manager.option('-n', '--name', dest='name')
def add_user_to_role(username, name):
    user = CMSUser.query.filter_by(username=username).first()
    if user:
        # role = CMSRole.query.filter_by(name=name).first()
        role = CMSRole.query.filter(CMSRole.name == name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print('用户添加到角色成功！')
        else:
            print('没有这个角色：%s' % role)
    else:
        print('用户:%s不存在!' % username)


if __name__ == '__main__':
    manager.run()
    '''数据库'''
    # 初始化迁移环境:python3 manage.py db init
    # 迁移数据库:python3 manage.py db migrate
    # 映射数据库:python3 manage.py db upgrade
    # 回滚:
    # ps:先备份数据
    #       python3 manage.py db history
    #       python3 manage.py db downgrade id
    '''CMS角色'''
    # 创建后台管理角色:python3 manage.py create_role
    '''CMS用户'''
    # 创建后台管理用户:python3 manage.py create_cms_user -u yyx -p 666666
    '''权限'''
    # 为角色添加权限:python3 manage.py add_user_to_role -u yyx -n 开发者
    '''测试'''
    # 测试权限控制:python3 manage.py test_permission

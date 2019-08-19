# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 上午9:32
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : manage.py
# @Software: PyCharm

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from zlbbs import create_app
from exts import db
from apps.cms import models as cms_models
from apps.front import models as front_models
from apps.models import BannerModel, BoardModel, PostModel
from apps import models

# cms
CMSUser = cms_models.CMSUser
CMSRole = cms_models.CMSRole
CMSPermission = cms_models.CMSPersmission

# front
FrontUser = front_models.FrontUser

app = create_app()
# 实例
manager = Manager(app)
# 绑定
Migrate(app, db)
# 添加命令
manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('cms用户添加成功')


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
    developer = CMSRole(name='开发者', desc='开发人员专用角色。')
    developer.permissions = CMSPermission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()
    print('角色创建完成')


@manager.option('-e', '--email', dest='email')
@manager.option('-n', '--name', dest='name')
def add_user_to_role(email, name):
    user = CMSUser.query.filter_by(email=email).first()
    if user:
        role = CMSRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print('用户添加到角色成功！')
        else:
            print('没有这个角色：%s' % role)
    else:
        print('%s邮箱没有这个用户!' % email)


@manager.command
def test_permission():
    user = CMSUser.query.first()
    # if user.is_developer:
    if user.has_permission(CMSPermission.VISITOR):
        print('这个用户有访问者的权限！')
    else:
        print('这个用户没有访问者权限！')


@manager.option('-t', '--telephone', dest='telephone')
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
def create_front_user(telephone, username, password):
    user = FrontUser(telephone=telephone, username=username, password=password)
    db.session.add(user)
    db.session.commit()


@manager.command
def create_test_post():
    for x in range(1, 205):
        title = '标题%s' % x
        content = '内容：%s' % x
        board = BoardModel.query.first()
        author = FrontUser.query.first()
        post = PostModel(title=title, content=content)
        post.board = board
        post.author = author
        db.session.add(post)
        db.session.commit()
    print('恭喜！测试帖子添加成功！')


if __name__ == '__main__':
    manager.run()
    '''数据库'''
    # 初始化迁移环境:python3 manage.py db init
    # 迁移数据库:python3 manage.py db migrate
    # 映射数据库:python3 manage.py db upgrade
    '''管理后台'''
    # 创建后台管理角色:python3 manage.py create_role
    # 创建后台管理用户:python3 manage.py create_cms_user -u test1 -p 666666 -u 1@qq.com
    # 为角色添加权限:python3 manage.py add_user_to_role -e 1@qq.com -n 运营
    # 测试权限控制:python3 manage.py test_permission
    '''用户端'''
    # 创建用户:python3 manage.py create_front_user -t 15013038819 -u yyx -p 666666

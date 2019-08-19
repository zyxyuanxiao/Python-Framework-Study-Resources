#!/usr/bin/env python
# encoding: utf-8

# 终端脚本
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from exts import db
from app.models import Profile
# from app.models import Gambler, Monitor, Match, Article, Push, User, Profile

manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    # /Users/yangyuexiong/Desktop/game_client
    # 初始化迁移环境：python3 manage.py db init
    # 迁移数据库：python3 manage.py db migrate
    # 映射数据库：python3 manage.py db upgrade
    # python3 manage.py db migrate -m "initial migration"

#!/usr/bin/env bash

set_production_config(){
    echo "初始化迁移环境"
    python3 manage.py db init
    echo "迁移数据库"
    python3 manage.py db migrate
    echo "映射数据库"
    python3 manage.py db upgrade
    echo "创建后台管理角色"
    python3 manage.py create_role
    echo "创建后台管理用户"
    python3 manage.py create_cms_user -u yyx -p 666666
    echo "为角色添加权限"
    python3 manage.py add_user_to_role -u yyx -n '开发者'
}

echo "-----func start-----"
cd /srv
. flask-env/bin/activate
cd /srv/HuntingBall
export PYTHONIOENCODING=utf-8
set_production_config
echo "-----func end-----"
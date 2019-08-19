#!/usr/bin/env bash

mapping(){
    echo "迁移数据库"
    python3 manage.py db migrate
    echo "映射数据库"
    python3 manage.py db upgrade

}

echo "-----ORM start-----"
cd /srv
. flask-env/bin/activate
cd /srv/HuntingBall
mapping
echo "-----done-----"

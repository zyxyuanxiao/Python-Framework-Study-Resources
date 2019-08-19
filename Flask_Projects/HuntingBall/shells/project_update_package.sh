#!/usr/bin/env bash

install_project_package(){
    cd /srv
    . flask-env/bin/activate
    cd /srv/HuntingBall
    pip3 install -r requirements.txt

}

echo "-----更新-安装:项目依赖包-----"
install_project_package
echo "-----done-----"
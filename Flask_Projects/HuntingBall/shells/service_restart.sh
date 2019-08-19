#!/usr/bin/env bash

echo "拉取最新代码"
git pull origin master
echo "重启-Nginx"
service nginx restart
echo "重启-supervisor"
supervisorctl update
supervisorctl reload
echo "utf-8"
cd /srv/HuntingBall
export PYTHONIOENCODING=utf-8



#!/usr/bin/env python
# encoding: utf-8

from flask_sqlalchemy import SQLAlchemy


# 连续写入
class RecordLogs(object):
    def __init__(self, msg, p):
        self.msg = msg
        self.p = p
        with open(p, 'a+') as f:
            f.write(msg)


p = '/root/game_control/phone_msg.txt'
# p = '/root/myproject/phone_msg.txt'
p1 = '/Users/yangyuexiong/Desktop/flask_ok1/phone_msg.txt'
db = SQLAlchemy()

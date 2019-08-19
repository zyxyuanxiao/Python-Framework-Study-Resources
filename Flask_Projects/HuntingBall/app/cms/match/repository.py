# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 下午3:55
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : repository.py
# @Software: PyCharm

from exts import db
import threading
from flask import abort


class MatchModel(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(MatchModel, '_instance'):
            with MatchModel._instance_lock:
                if not hasattr(MatchModel, '_instance'):
                    MatchModel._instance = object.__new__(cls)
        return MatchModel._instance

    def __init__(self, obj):
        self.obj = obj

    def add(self):
        try:
            db.session.add(self.obj)
            db.session.commit()
        except BaseException as e:
            print('数据库异常:%s' % e)
            abort(503)
        return True

    @staticmethod
    def up(args):
        try:
            db.session.commit()
        except BaseException as e:
            print('数据库异常:%s' % e)
            abort(503)
        return True

    @staticmethod
    def delete(*args):
        try:
            db.session.commit()
        except BaseException as e:
            print('数据库异常:%s' % e)
            abort(503)
        return True


if __name__ == '__main__':
    # test instance
    o = 1


    def task(arg):
        obj = MatchModel(o)
        print(arg)
        print(obj)


    for i in range(10):
        t = threading.Thread(target=task, args=[i])
        t.start()

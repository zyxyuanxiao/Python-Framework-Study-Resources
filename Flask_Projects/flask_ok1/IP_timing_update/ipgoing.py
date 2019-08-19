# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午3:40
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : ipgoing.py
# @Software: PyCharm

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


app = create_app()
app.app_context().push()

from qqwry import QQwry
import datetime
from myapp.models import IpList
from qqwry import updateQQwry

nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(nowTime)

q = QQwry()
q.load_file('/Users/yangyuexiong/Desktop/flask_okc1/IP_timing_update/www.NewXing.com/qqwry.dat')

result = q.lookup('59.42.39.14')
print(result)

x = result[0]
y = result[1]
print(x, y)
print(x[0:3], x[3:6], x[6:9])

if __name__ == '__main__':
    pass

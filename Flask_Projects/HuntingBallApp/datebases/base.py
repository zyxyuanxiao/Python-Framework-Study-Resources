# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 4:51 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : base.py
# @Software: PyCharm


import pymysql


# def select():
#     sql = "select * from t_users where email='%s'" % acc


class CRUD:

    def __init__(self, host, user, password, db, port):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        d = pymysql.connect(host=self.host, user=self.user,
                            password=self.password, db=self.db, port=self.port)
        self.d = d

        self.d.cursor()
        self.d.ping(reconnect=True)

    def C(self, sql):
        print(self.d.password)

    def R(self):
        pass

    def U(self):
        pass

    def D(self):
        pass


if __name__ == '__main__':
    obj = CRUD('localhost', 'root', '123456', 'HuntingBall', 3306)
    # print('1---', obj)
    s = "select * from gambler where tel='15013038819'"
    print(obj.C(s))

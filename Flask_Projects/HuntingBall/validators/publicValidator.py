# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 下午5:44
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : publicValidator.py
# @Software: PyCharm


from utils.apiResult import ex_er


def is_valid(data):
    for i, j in data.items():
        if data[i] == '':
            ex_er(1005)
    return True


def is_valid2(data):
    for i, j in data.items():
        if i == 'tel':
            if len(data[i]) != 11:
                print(i, '< 11')
        if i == 'password':
            if len(data[i]) < 6:
                print(i, '< 6')
    from app.api.user.models import Gambler
    u = Gambler.query.filter_by(username=data["tel"]).first()
    return True


d = {
    "tel": "11111111111",
    "password": "b",
}

if __name__ == '__main__':
    is_valid2(d)

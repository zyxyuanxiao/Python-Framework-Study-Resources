# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 下午3:17
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : tool.py
# @Software: PyCharm

import re


# 序列化
def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d


# 手机号正则
def tels(m):
    k = re.match('1[34578]\\d{9}', m)
    if k:
        return True
    else:
        return False


# 单例
class IndividualExample:
    import threading
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(IndividualExample, '_instance'):
            with IndividualExample._instance_lock:
                if not hasattr(IndividualExample, '_instance'):
                    IndividualExample._instance = object.__new__(cls)
        return IndividualExample._instance


# 字典value切片
def cut_value(arg):
    ret = {}
    for key, value in arg.items():
        # print(key)
        # print(value)
        if len(value) > 20 and key != 'image_path':
            ret[key] = value[0:20]
        else:
            ret[key] = value
    return ret

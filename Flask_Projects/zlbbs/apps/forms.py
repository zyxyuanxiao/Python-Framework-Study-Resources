# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 下午4:06
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : forms.py
# @Software: PyCharm

from wtforms import Form


class BaseForm(Form):
    def get_error(self):
        message = self.errors.popitem()[1][0]
        return message

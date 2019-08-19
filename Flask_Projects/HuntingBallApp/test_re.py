# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 5:56 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_re.py
# @Software: PyCharm

import re

pattern = re.compile(r'\d+')
m = pattern.match('12a3')
print(m.group())

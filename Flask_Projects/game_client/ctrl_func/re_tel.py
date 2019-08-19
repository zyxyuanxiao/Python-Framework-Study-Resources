#!/usr/bin/env python
# encoding: utf-8
import re


# m = '1277777777771111'
# k = re.match('1[3458]\\d{9}', m)
# print(k)
# if k:
#     print('okc')


def tels(m):
    k = re.match('1[34578]\\d{9}', m)
    if k:
        return True
    else:
        return False


# m = '0.00'
# m2 = '01'
# m3 = '0.10'
# k = re.match('^(([1-9]\d{0,9})|0)(\.\d{1,2})?$', m)
# k2 = re.match('^(([1-9]\d{0,9})|0)(\.\d{1,2})?$', m2)
# k3 = re.match('^(([1-9]\d{0,9})|0)(\.\d{1,2})?$', m3)
#
# print(k)
# print(k2)
# print(k3)
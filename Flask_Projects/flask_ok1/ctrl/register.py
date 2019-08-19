#!/usr/bin/env python
# encoding: utf-8

from ctrl.ApiResult import *


class Register(object):
    def __init__(self, gambler, username, password):
        self.gambler = gambler
        self.username = username
        self.password = password


class Rpass(object):
    def Rfunc(self, okc):

        if okc.gambler != None:
            return ApiResult().formattingData(status=0, msg='该号码已经注册!', data=[])

        if okc.username == '':
            return ApiResult().formattingData(status=1, msg='手机号不能为空!', data=[])

        if len(okc.username) != 11:
            return ApiResult().formattingData(status=2, msg='手机长度应为11位数字!', data=[])
        try:
            m = int(okc.username)
            if type(m) != type(1):
                pass
        except Exception as e:
            return ApiResult().formattingData(status=3, msg='手机号应为数字', data={})

        if okc.password == '':
            return ApiResult().formattingData(status=4, msg='登陆密码不能为空!', data=[])

        if len(okc.password) < 6 or len(okc.password) > 14:
            return ApiResult().formattingData(status=5, msg='登陆密码少于6位或多于14!', data=[])

        # if okc.pay_password == '':
        #     return ApiResult().formattingData(status=6, msg='支付密码不能为空!', data=[])
        #
        # if len(okc.pay_password) != 6:
        #     return ApiResult().formattingData(status=7, msg='支付密码应为6位数字!', data=[])

        # try:
        #     p = int(okc.pay_password)
        #     if type(p) != type(1):
        #         pass
        # except Exception as e:
        #     return ApiResult().formattingData(status=8, msg='支付密码应为数字!', data=[])

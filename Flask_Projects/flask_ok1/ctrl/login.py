#!/usr/bin/env python
# encoding: utf-8
from ctrl.ApiResult import *


class Login(object):
    def __init__(self, user, mobile, password):
        self.user = user
        self.mobile = mobile
        self.password = password


class Lpass(object):
    def Lfunc(self, okc):

        if not okc.user:
            return ApiResult().formattingData(status=403, msg='手机号未注册', data={})

        if okc.password != okc.user.password:
            return ApiResult().formattingData(status=405, msg='密码错误', data={})

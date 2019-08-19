#!/usr/bin/env python
# encoding: utf-8
from ctrl_func.ApiResult import *


def vip(func):  # 传入被装饰的函数
    def inner(*args):
        d = func().data
        x = d.decode()
        y = eval(x)
        status = y.get('status')
        print('status', status)
        if status == 2:
            print('会员用户')
            return func(*args)
        elif status == 1:
            print('普通用户')
            i = y.get('data')
            for k in i:
                level = k.get('level')
                print('level', level)
                if level == 1:
                    print('这是普通用户需要充值')
                return ApiResult().formattingData(status=403, msg='成为会员开启此功能', data=[])

    return inner


def app_vip_decorator(func):

    def wrapper(push_id):
        d = func(push_id).data
        x = d.decode()
        y = eval(x)
        # print(y)
        status = y.get('status')
        # print('status', status)
        if status == 404:
            return ApiResult().formattingData(status=404, msg='未找到对应的推荐内页', data=[])
        if status == 2:
            # print('会员用户')
            return func(push_id)
        elif status == 1:
            # print('普通用户')
            i = y.get('data')
            # print(i)
            for k in i:
                level = k.get('level')
                # print('level', level)
                if level == 1:
                    print('这是普通用户需要充值')
                return ApiResult().formattingData(status=403, msg='成为会员开启此功能', data=[])

    return wrapper

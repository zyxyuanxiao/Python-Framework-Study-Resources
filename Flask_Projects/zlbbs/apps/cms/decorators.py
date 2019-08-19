# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 下午1:42
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : decorators.py
# @Software: PyCharm

from flask import session, redirect, url_for, g
from functools import wraps
import config


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if config.CMS_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('cms.login'))

    return inner


def permission_required(permission):
    def outter(func):
        @wraps(func)
        def inner(*args, **kwargs):
            user = g.cms_user
            if user.has_permission(permission):
                return func(*args, **kwargs)
            else:
                return redirect(url_for('cms.index'))

        return inner

    return outter
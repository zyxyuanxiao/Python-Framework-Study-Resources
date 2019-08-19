# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 下午2:43
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : hooks.py
# @Software: PyCharm

from .views import bp
from flask import session, g
from .models import CMSUser, CMSPersmission
import config


# 请求前执行
@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        print('user_id', user_id)
        user = CMSUser.query.get(user_id)
        print('user', user)
        if user:
            g.cms_user = user


# 上下文
@bp.context_processor
def cms_context_processor():
    return {"CMSPermission": CMSPersmission}

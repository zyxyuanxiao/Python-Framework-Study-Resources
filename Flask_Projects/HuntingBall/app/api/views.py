# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 下午3:37
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : views.py
# @Software: PyCharm

from flask import Blueprint, abort, request, g
from exts import auth, auth2

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/')
def index():
    # abort(503)
    return 'This Api Blueprint'


users = [
    {'username': 'Tom', 'password': '111111'},
    {'username': '1', 'password': '1'}
]


@auth.get_password
def get_password(username):
    for user in users:
        if user['username'] == username:
            return user['password']
    return None


@bp.route('/l')
@auth.login_required
def index2():
    return "Hello, %s!" % auth.username()


tokens = {
    "secret-token-1": "John",
    "secret-token-2": "Susan"
}


@auth2.verify_token
def verify_token(token):
    g.user = None
    if token in tokens:
        g.user = tokens[token]
        return True
    return False


@bp.route('/t')
@auth2.login_required
def index3():
    return "Hello, %s!" % g.user

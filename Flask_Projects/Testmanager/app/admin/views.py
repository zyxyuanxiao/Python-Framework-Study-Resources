# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 下午7:37
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : views.py
# @Software: PyCharm

from . import admin
from flask import render_template, redirect, url_for, session, request
from app.admin.forms import LoginForm
from functools import wraps


def admin_login_req(f):
    @wraps(f)
    def d_fun(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login', next=request.ur))
        return f(*args, **kwargs)

    return d_fun


@admin.route('/', methods=['GET'])
def index():
    return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data['account']).first()
    return render_template('admin/login.html', form=form)


@admin.route('/logout', methods=['GET', 'POST'])
def logout():
    return redirect(url_for('login'))


@admin.route('/pwd', methods=['GET', 'POST'])
def pwd():
    return render_template('admin/pwd.html')


@admin.route('/tag/add', methods=['GET', 'POST'])
def tag_add():
    return render_template('admin/tag_add.html')


@admin.route('/tag/list', methods=['GET', 'POST'])
def tag_list():
    return render_template('admin/tag_list.html')


@admin.route('/movie/add', methods=['GET', 'POST'])
def movie_add():
    return render_template('admin/movie_add.html')


@admin.route('/movie/list', methods=['GET', 'POST'])
def movie_list():
    return render_template('admin/movie_list.html')


@admin.route('/preview/add', methods=['GET', 'POST'])
def preview_add():
    return render_template('admin/preview_add.html')


@admin.route('/preview/list', methods=['GET', 'POST'])
def preview_list():
    return render_template('admin/preview_list.html')


@admin.route('/user/list', methods=['GET', 'POST'])
def user_list():
    return render_template('admin/user_list.html')


@admin.route('/user/view', methods=['GET', 'POST'])
def user_view():
    return render_template('admin/user_view.html')


@admin.route('/comment/list', methods=['GET', 'POST'])
def comment_list():
    return render_template('admin/comment_list.html')


@admin.route('/moviecol/list', methods=['GET', 'POST'])
def moviecol_list():
    return render_template('admin/moviecol_list.html')


@admin.route('/oplog/list', methods=['GET', 'POST'])
def oplog_list():
    return render_template('admin/oplog_list.html')


@admin.route('/adminloginlog/list', methods=['GET', 'POST'])
def adminloginlog_list():
    return render_template('admin/adminloginlog_list.html')


@admin.route('/userloginlog/list', methods=['GET', 'POST'])
def userloginlog_list():
    return render_template('admin/userloginlog_list.html')


@admin.route('/auth/add', methods=['GET', 'POST'])
def auth_add():
    return render_template('admin/auth_add.html')


@admin.route('/auth/list', methods=['GET', 'POST'])
def auth_list():
    return render_template('admin/auth_list.html')


@admin.route('/role/add', methods=['GET', 'POST'])
def role_add():
    return render_template('admin/role_add.html')


@admin.route('/role/list', methods=['GET', 'POST'])
def role_list():
    return render_template('admin/role_list.html')


@admin.route('/admin/add', methods=['GET', 'POST'])
def admin_add():
    return render_template('admin/admin_add.html')


@admin.route('/admin/list', methods=['GET', 'POST'])
def admin_list():
    return render_template('admin/admin_list.html')

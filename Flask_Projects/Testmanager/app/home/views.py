# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 下午7:37
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : views.py
# @Software: PyCharm

from . import home
from flask import render_template


@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/login')
def login():
    return render_template('home/login.html')


@home.route('/register')
def register():
    return render_template('home/register.html')


@home.route('/logout')
def logout():
    return render_template('home/logout.html')


@home.route('/user')
def user():
    return render_template('home/user.html')


@home.route('/pwd')
def pwd():
    return render_template('home/pwd.html')


@home.route('/comments')
def comments():
    return render_template('home/comments.html')


@home.route('/loginlog')
def loginlog():
    return render_template('home/loginlog.html')


@home.route('/moviecol')
def moviecol():
    return render_template('home/moviecol.html')


@home.route('/animation')
def animation():
    return render_template('home/animation.html')


@home.route('/search')
def search():
    return render_template('home/search.html')


@home.route('/play')
def play():
    return render_template('home/play.html')

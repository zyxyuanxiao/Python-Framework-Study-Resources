# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 上午9:29
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : __init__.py.py
# @Software: PyCharm

from .views import bp
from .userLogin.views import LoginView
from .match.views import MatchView
from .article.views import ArticleViews

bp.add_url_rule('/login', view_func=LoginView.as_view('login'))
bp.add_url_rule('/match', view_func=MatchView.as_view('match'))
bp.add_url_rule('/match/<pageIndex>/<pageSize>', view_func=MatchView.as_view('matchs'))
bp.add_url_rule('/article', view_func=ArticleViews.as_view('article'))

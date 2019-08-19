# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 下午3:14
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : views.py
# @Software: PyCharm

from flask import views, request
from .service import MatchService
from .repository import MatchModel
from utils.apiResult import api_result
from app.cms.views import bp
from app.cms.userLogin.cms_decorators import login_required


@bp.route('/xxx')
def xxx():
    from app.cms.userLogin.models import Article, CMSUser
    x = CMSUser.query.filter_by(username='yyx').first()
    print(x)
    print(x.articles[0].title, type(x.articles), type(x.articles[0]))
    a = Article.query.filter_by(id=1).first()
    print(a)
    print(a.user.id)
    print(a.user.username)
    print(a.user.articles, type(a.user.articles[0]))
    return 'text import bp'


class MatchView(views.MethodView):
    # decorators = [login_required]

    def get(self):
        data = request.args.to_dict()
        return api_result(code=200, message='', data=MatchService().read(data))

    @login_required
    def post(self):
        data = request.get_json()
        match = MatchService().add_match(data)
        if MatchModel(match).add():
            return api_result(code=201, message='', data=data)

    @login_required
    def put(self):
        data = request.get_json()
        m = MatchService().up_match(data)
        match = MatchModel.up(m)
        if match:
            return api_result(code=200, message='update ok', data=[])

    @login_required
    def delete(self):
        data = request.get_json()
        m = MatchService().del_match(data)
        match = MatchModel.delete(m)
        if match:
            return api_result(code=204, message='delete ok', data=[])

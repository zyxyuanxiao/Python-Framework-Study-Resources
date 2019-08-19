# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 上午12:06
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : views.py
# @Software: PyCharm

from flask import views, request
from .service import ArticleService
from utils.apiResult import api_result
from utils.tool import row2dict
from app.cms.article.models import Article


class ArticleViews(views.MethodView):

    def get(self):
        data = request.args.to_dict()
        a = Article.query.all()
        arr = []
        for i in a:
            arr.append(row2dict(i))

        return api_result(code=200, message='cms-article-all-list', data=arr)

    def post(self):
        data = request.get_json()
        # print('data', data)
        new_article = ArticleService.add_article(data)
        return api_result(code=201, message='创建成功', data=new_article)

    def put(self):
        pass

    def delete(self):
        pass

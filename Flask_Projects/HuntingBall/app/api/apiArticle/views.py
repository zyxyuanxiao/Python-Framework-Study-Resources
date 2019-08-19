# -*- coding: utf-8 -*-
# @Time    : 2018/9/9 下午1:38
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : views.py
# @Software: PyCharm

from flask_restful import Resource
from flask import request
from .service import ArticleService
from utils.apiResult import api_result, ex_er


class ArticleApi(Resource):

    def get(self):
        data = request.args.to_dict()

        if 'article_id' in data.keys():
            # print('获取文章：内页')
            a = ArticleService.get_article_page(data)
            return api_result(code=200, message='', data=a)
        if 'pageIndex' and 'pageSize' and 'state' in data.keys():
            # print('获取文章：列表')
            return api_result(code=200, message='', data=ArticleService.get_articles(data))
        else:
            ex_er(1006)

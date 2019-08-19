# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 上午12:11
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : service.py
# @Software: PyCharm

from app.cms.article.models import Article
from validators.publicValidator import is_valid


class ArticleService(object):

    @staticmethod
    def add_article(data):
        if is_valid(data):
            return Article.get_json(data)

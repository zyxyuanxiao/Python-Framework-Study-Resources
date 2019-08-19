# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 上午12:11
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : service.py
# @Software: PyCharm

from flask import g
from app.cms.article.models import Article
from utils.apiResult import ex_er
from utils.tool import row2dict, cut_value
from validators.publicValidator import is_valid


class ArticleService(object):

    @staticmethod
    def add_article(data):
        if is_valid(data):
            a = Article.get_json(data)
        return True, a

    @staticmethod
    def get_articles(data):
        arr = []
        page = int(data['pageIndex'])
        size = int(data['pageSize'])
        if int(data['state']) == 1:
            pagination = Article.query.filter_by(a_status='1', state='1').order_by('cea_time').paginate(page,
                                                                                                        per_page=int(
                                                                                                            size),
                                                                                                        error_out=False)
            p = pagination.items
            t = pagination.total
            for i in p:
                article = cut_value(row2dict(i))
                arr.append(article)
            d = {
                'records': arr,
                'now_page': page,
                'totalAmount': t
            }
            return d

        if int(data['state']) == 2:
            pagination = Article.query.filter_by(a_status='1', state='2').order_by('cea_time').paginate(page,
                                                                                                        per_page=int(
                                                                                                            size),
                                                                                                        error_out=False)
            p = pagination.items
            t = pagination.total
            for i in p:
                article = cut_value(row2dict(i))
                arr.append(article)
            d = {
                'records': arr,
                'now_page': page,
                'totalAmount': t
            }
            return d
        else:
            ex_er(1006)

    @staticmethod
    def get_article_page(data):
        article = Article.query.filter_by(id=data['article_id']).first()
        if not article:
            ex_er(1006)
        if int(article.state) == 1:
            # print(article.to_dict())
            return article.to_dict()
        if int(article.state) == 2:
            # print('收费文章')
            if hasattr(g.app_user, 'level'):
                pass
                # print('level:%s' % g.app_user.level, type(g.app_user.level))
            else:
                ex_er(401)
            if int(g.app_user.level) == 2:
                return article.to_dict()
            else:
                # print('不是会员')
                ex_er(403)

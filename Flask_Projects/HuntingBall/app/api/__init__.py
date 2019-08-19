# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 上午9:29
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask_restful import Api, Resource
from .views import bp
from . import hooks
from .user.views import UserRegisterApi, UserLoginApi, Test
from .apiArticle.views import ArticleApi

api = Api(bp)
api.add_resource(UserRegisterApi, '/register/', '/register/<user_id>', endpoint='register')
api.add_resource(UserLoginApi, '/login/', '/login/<user_id>/<token>', endpoint='login')
api.add_resource(Test, '/test', endpoint='test')
api.add_resource(ArticleApi, '/article', '/article/<pageIndex>/<pageSize>/<state>', '/article/<article_id>',
                 endpoint='article')

api.init_app(bp)


@api.resource('/foo')
class Foo(Resource):
    def get(self):
        print(self)
        print(self.methods)
        print(self.as_view)
        print(self.decorators)
        print(self.provide_automatic_options)
        print(self.representations)
        print(type(self))
        return 'Hello, World!'

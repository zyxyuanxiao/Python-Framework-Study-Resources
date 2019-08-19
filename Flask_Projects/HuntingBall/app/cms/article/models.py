# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 下午2:51
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : models.py
# @Software: PyCharm

from exts import db


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(128), nullable=False)
    vs_category = db.Column(db.String(128), nullable=False)
    vs_other_c = db.Column(db.String(128), nullable=True)
    vs = db.Column(db.String(128), nullable=False)
    al = db.Column(db.String(128), nullable=False)
    link = db.Column(db.String(128), nullable=True)
    content = db.Column(db.Text)
    vs_push = db.Column(db.String(128), nullable=True)
    state = db.Column(db.String(128), nullable=True)
    image_name = db.Column(db.String(128))
    image_path = db.Column(db.String(256))
    a_status = db.Column(db.String(128), default='1')
    watch = db.Column(db.String(128), default='999')
    cea_time = db.Column(db.DateTime, server_default=db.func.now())

    uid = db.Column(db.Integer, db.ForeignKey('cms_user.id'))

    def __repr__(self):
        return '<article: 文章[id:%s] 作者[id:%s]>' % (
            self.id,
            self.uid,
        )

    def get_json(self):
        a = Article(
            title=self['title'],
            author=self['author'],
            vs_category=self['vs_category'],
            vs_other_c=self['vs_other_c'],
            vs=self['vs'],
            al=self['al'],
            link=self['link'],
            content=self['content'],
            vs_push=self['vs_push'],
            state=self['state'],
            image_name=self['image_name'],
            image_path=self['image_path'],
            a_status=self['a_status'],
            watch=self['watch'],
            uid=self['uid'],
        )
        db.session.add(a)
        db.session.commit()
        data = {
            'id': a.id,
            'title': a.title,
            'author': a.author,
            'vs_category': a.vs_category,
            'vs_other_c': a.vs_other_c,
            'vs': a.vs,
            'al': a.al,
            'link': a.link,
            'content': a.content,
            'vs_push': a.vs_push,
            'state': a.state,
            'image_name': a.image_name,
            'image_path': a.image_path,
            'a_status': a.a_status,
            'watch': a.watch,
            'cea_time': a.cea_time,
            'uid': a.uid,
            'uid->username': a.user.username,
        }
        return data

    def to_dict(self):
        article_dict = {}
        article_dict['id'] = self.id
        article_dict['title'] = self.title
        article_dict['author'] = self.author
        article_dict['vs_category'] = self.vs_category
        article_dict['vs_other_c'] = self.vs_other_c
        article_dict['vs'] = self.vs
        article_dict['al'] = self.al
        article_dict['link'] = self.link
        article_dict['content'] = self.content
        article_dict['vs_push'] = self.vs_push
        article_dict['state'] = self.state
        article_dict['image_name'] = self.image_name
        article_dict['image_path'] = self.image_path
        article_dict['a_status'] = self.a_status
        article_dict['watch'] = self.watch
        article_dict['cea_time'] = self.cea_time
        article_dict['uid'] = self.uid
        article_dict['uid->username'] = self.user.username
        return article_dict

# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 上午11:05
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : demo1.py
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DECIMAL, Enum, Text, func, or_, all_, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
import enum
import random

# mysql数据库
HOSTNAME = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = 'lieqiu'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()
print(Base)

# 判断是否成功
conn = engine.connect()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=True)

    # uselist：关闭一对多
    # extend = relationship('UserExtend', uselist=False)

    def __repr__(self):
        return "<User(username:%s)>" % self.username


class UserExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50))
    uid = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", backref=backref("extend", uselist=False))  # uselist：关闭一对多


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    uid = Column(Integer, ForeignKey("user.id"), onupdate='')

    # backref:反向引用 为User添加articles属性
    author = relationship('User', backref='articles')

    def __repr__(self):
        return "<Article(title:%s,content=%s)>" % (self.title, self.content)


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(username='zhiliao')
# article = Article(title='one', content='aaa')
# article.author = user
# print(article.author)
# session.add(user)
# session.commit()

ux = session.query(Article).filter(Article.author).all()
print(ux)

u = session.query(User).filter(User.articles).all()
print(u)

# article = Article(title='abc', content='123', uid=1)
# session.add(article)
# session.commit()

# article = session.query(Article)
# print(article)

# article = session.query(Article).first()
# print(article.author)
#
# user = session.query(User).first()
# print(user.articles)

# user = User(username='zhiliao')
# a1 = Article(title='a', content='A')
# a2 = Article(title='a2', content='A2')
#
# user.articles.append(a1)
# user.articles.append(a2)
# user = session.query(User).filter(User.id == 1).first()
# a3 = Article(title='a2222', content='A2222')
# a3.author = user
# session.add(a3)
# session.commit()

# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 上午11:05
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : demo1.py
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DECIMAL, Enum, Text, func, or_, all_, \
    ForeignKey, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
import enum
import random
from datetime import datetime

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


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.now)
    uid = Column(Integer, ForeignKey("user.id"))

    author = relationship("User", backref=backref("articles", lazy='dynamic'))

    __mapper_args__ = {
        "order_by": create_time.desc()
    }

    def __repr__(self):
        return "<Article(title:%s,create_time:%s)>" % (self.title, self.create_time)


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# u = User(username='yyx')
# for i in range(1, 101):
#     title = 'title %s' % i
#     a = Article(title=title)
#     a.author = u
#     session.add(a)
# session.commit()

u = session.query(User).first()
print(u.articles)
print(type(u.articles))
print(u.articles.filter(Article.id > 99).all())
# a = Article(title='title 101')
# u.articles.append(a)
# session.commit()
a = session.query(func.count(Article.id)).first()
print(a)
# a = session.query(Article).limit(10).all()
# print(a)
# a = session.query(Article).offset(0).limit(10).all()
# b = session.query(Article)[0:10]
# c = session.query(Article).slice(0, 10).all()
# print(a)
# print('\n')
# print(b)
# print('\n')
# print(c)

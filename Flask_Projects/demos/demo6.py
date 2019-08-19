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

    def __repr__(self):
        return "<User(username: %s)>" % self.username


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.now)
    uid = Column(Integer, ForeignKey("user.id"))

    author = relationship("User", backref="articles")

    def __repr__(self):
        return "<Article(title: %s)>" % self.title


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user1 = User(username='zhiliao')
# user2 = User(username='ketang')
#
# for x in range(1):
#     article = Article(title='title %s' % x)
#     article.author = user1
#     session.add(article)
# session.commit()
#
#
# for x in range(1,3):
#     article = Article(title='title %s' % x)
#     article.author = user2
#     session.add(article)
# session.commit()

if __name__ == '__main__':
    # r = session.query(User.username, func.count(Article.id)).join(Article, User.id == Article.uid).group_by(
    #     func.count(Article.id)).all()
    # print(r)
    result = session.query(User, func.count(Article.id)).join(Article).group_by(User.id).order_by(
        func.count(Article.id).desc()).all()
    print(result)

    result = session.query(User).join(Article).group_by(User.id).order_by(
        func.count(Article.id).desc()).all()
    print(result)
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 上午11:05
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : demo1.py
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DECIMAL, Enum, Text, func, or_, all_, \
    ForeignKey, Table
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

article_tag = Table(
    'article_tag',
    Base.metadata,
    Column('article_id', Integer, ForeignKey('article.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True),
)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)

    tags = relationship('Tag', backref='articles', secondary='article_tag')

    def __repr__(self):
        return "<Article(title:%s)>" % self.title


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Tag(name:%s)>" % self.name


# Base.metadata.drop_all()
# Base.metadata.create_all()
# a1 = Article(title='a1')
# a2 = Article(title='a2')
#
# t1 = Tag(name='t1')
# t2 = Tag(name='t2')
#
# a1.tags.append(t1)
# a1.tags.append(t2)
#
# a2.tags.append(t1)
# a2.tags.append(t2)
#
# session.add(a1)
# session.add(a2)
# session.commit()

a = session.query(Article).filter(Article.id == 1).first()
print(a.title)
print(a.tags)

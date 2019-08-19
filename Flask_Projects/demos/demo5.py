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
    age = Column(Integer, default=0)
    gender = Column(Enum("male", "female", "secret"), default="male")


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# u1 = User(username='y1', age=18, gender='male')
# u2 = User(username='y2', age=18, gender='male')
# u3 = User(username='y3', age=20, gender='female')
# u4 = User(username='y4', age=22, gender='female')
# u5 = User(username='y5', age=30, gender='female')
#
# session.add_all([u1, u2, u3, u4, u5])
# session.commit()

if __name__ == '__main__':
    # group_by
    r = session.query(User.age, func.count(User.id)).group_by(User.age).all()
    print(r)
    # having
    r = session.query(User.age, func.count(User.id)).group_by(User.age).having(User.age < 19).all()
    print(r)

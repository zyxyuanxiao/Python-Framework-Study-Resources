# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 上午11:05
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : demo1.py
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DECIMAL, Enum, Text, func, or_, all_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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


# r = conn.execute('select 1')
# print(r.fetchone())
class TagEnum(enum.Enum):
    python = 'python'
    flask = 'flask'
    django = 'django'


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)

    # is_delete = Column(Boolean)
    # price = Column(DECIMAL(10, 4))
    # tag = Column(Enum(TagEnum))
    # con = Column(Text)

    def __repr__(self):
        return '<person:name %s age %s>' % (self.name, self.age)


# Base.metadata.drop_all()
# Base.metadata.create_all()
# p = Person(is_delete=False)
# p = Person(price=10000.1111)
# p = Person(tag=TagEnum.python)
# x = 100 * 100 * 100 * 100 * 1000
# p = Person(con=str(x))
# session.add(p)
# session.commit()

# for x in range(6):
#     p = Person(name='name%s' % x, age=random.randint(10, 20))
#     session.add(p)
# session.commit()

# a = session.query(Person).all()
# for i in a:
#     print(i)

# c = session.query(func.count(Person.id)).first()
# print(c)
#
# c1 = session.query(func.avg(Person.age)).first()
# print(c1)
#
# c2 = session.query(func.max(Person.age)).first()
# print(c2)
#
# c3 = session.query(func.min(Person.age)).first()
# print(c3)
#
# c4 = session.query(func.sum(Person.age)).first()
# print(c4)

# a = session.query(Person).filter(Person.id == 1).first()
# print(a)
#
# a1 = session.query(Person).filter(Person.id != 1).all()
# print(a1)

# a1 = session.query(Person).filter(Person.name.ilike('name%')).all()
# print(a1)

# a1 = session.query(Person).filter(Person.name.in_(['name0', 'name1'])).all()
# print(a1)
#
# a1 = session.query(Person).filter(Person.name.notin_(['name0', 'name1'])).all()
# print(a1)
#
# a1 = session.query(Person).filter(~Person.name.in_(['name0', 'name1'])).all()
# print(a1)

# a1 = session.query(Person).filter(Person.name == 'name0', Person.age == 20).all()
# print(a1)

a1 = session.query(Person).filter(or_(Person.name == 'name2', Person.age == 20)).all()
print(a1)

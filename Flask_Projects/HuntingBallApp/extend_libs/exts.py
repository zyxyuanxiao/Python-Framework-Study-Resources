# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 下午5:42
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : exts.py
# @Software: PyCharm


from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from contextlib import contextmanager
from flask_sqlalchemy import BaseQuery as _BaseQuery
from datetime import datetime


class SQLAlchemy(_SQLAlchemy):
    """
    使flask-SQLAlchemy对象自动支持commit()
    """

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class BaseQuery(_BaseQuery):
    """
    自定制flask-SQLAlchemy中的BaseQuery:默认添加status=1
    """

    def filter_by(self, **kwargs):
        if 'status' not in kwargs:  # 如果status字段不在fliter_by中,默认添加status=1
            kwargs['status'] = 1
        return super(BaseQuery, self).filter_by(**kwargs)  # 返回父类的fliter_by的执行


db = SQLAlchemy(query_class=BaseQuery)  # 在SQLAlchemy中注册一下query_class


class Base(db.Model):
    """
    status:状态
    create_timestamp:创建时间戳
    create_time:创建时间DateTime
    update_timestamp:更新时间戳
    update_time:更新时间DateTime
    """

    __abstract__ = True
    status = db.Column(db.Integer, default=1)
    create_time = db.Column(db.DateTime, server_default=db.func.now())
    create_timestamp = db.Column(db.String(128), default=int(datetime.now().timestamp()))
    update_time = db.Column(db.String(128), server_default='', onupdate=db.func.now())
    update_timestamp = db.Column(db.String(128), server_default='', onupdate=int(datetime.now().timestamp()))

    def __getitem__(self, item):
        return getattr(self, item)

    def to_dict(self):
        """
        对象转换dict
        """
        print('to_dict')
        obj_dict = {}
        # print(self.__table__.columns)
        for c in self.__table__.columns:
            # print(c, '--', c.name)
            # if c.name == 'create_timestamp' or c.name == 'update_timestamp' or c.name == 'create_time' or c.name == 'update_time':
            if c.name == 'create_time' or c.name == 'update_time':
                pass
            else:
                obj_dict[c.name] = getattr(self, c.name, None)
        # return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
        print(obj_dict)
        return obj_dict

    def keys(self):

        return self.fields

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def delete(self):
        self.status = 2

    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self

    def append(self, *keys):
        for key in keys:
            self.fields.append(key)
        return self

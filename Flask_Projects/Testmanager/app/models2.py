# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 下午8:06
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : models.py
# @Software: PyCharm

"""http://www.pythondoc.com/flask-sqlalchemy/config.html"""

from app import db

registrations = db.Table('registrations',
                         db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
                         db.Column('class_id', db.Integer, db.ForeignKey('classes.id'))
                         )


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    classes = db.relationship('Class',
                              secondary=registrations,
                              backref=db.backref('students', lazy='dynamic'),
                              lazy='dynamic')


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

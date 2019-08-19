# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 下午1:58
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : forms.py
# @Software: PyCharm

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class LoginForm(Form):
    """管理员登录"""
    account = StringField(
        label='帐号',
        validators=[
            DataRequired('请输入帐号')
        ],
        description='帐号',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入账号！',
            'required': 'required'
        }
    )
    pwd = PasswordField(
        label='密码',
        validators=[
            DataRequired('请输入密码')
        ],
        description='密码',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入密码！',
            # 'required': 'required'
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            'class': 'btn btn-primary btn-block btn-flat',
            # 'required': 'required'
        }
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError('帐号不存在')

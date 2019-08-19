# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 下午4:03
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : user_vali.py
# @Software: PyCharm

from app.api.userApi.models import Gambler
from flask import request
from wtforms import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import ValidationError, DataRequired, Length, EqualTo
from utils.apiResult import api_result, error_abort

from flask_wtf import FlaskForm


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    # def validate_for_api(self):
    #     valid = super(BaseForm, self).validate()
    #     if not valid:
    #         raise ParameterException(msg=self.errors)
    #     return self


class LoginForm(BaseForm):
    tel = StringField('tel', validators=[Length(11, 11)])
    password = StringField('password', validators=[Length(6, 16)])

    def validate_tel(self, field):
        if not self.get_user():
            raise ValidationError('Invalid tel!')

    def validate_password(self, field):
        if not self.get_user():
            return
        if not self.get_user().check_password(field.data):
            raise ValidationError('Incorrect password!')

    def get_user(self):
        return Gambler.query.filter_by(tel=self.tel.data).first()


if __name__ == '__main__':
    from app import create_app

    app = create_app()
    with app.app_context():
        data = {
            "tel": "15013038819",
            "password": "666666"
        }
        form = LoginForm(data=data)
        if form.validate():
            print('okc')
        else:
            print('no')

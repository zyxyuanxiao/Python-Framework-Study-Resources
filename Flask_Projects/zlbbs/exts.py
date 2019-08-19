# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 上午9:32
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : exts.py
# @Software: PyCharm

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from utils.alidayu import AlidayuAPI

db = SQLAlchemy()
mail = Mail()
alidayu = AlidayuAPI()

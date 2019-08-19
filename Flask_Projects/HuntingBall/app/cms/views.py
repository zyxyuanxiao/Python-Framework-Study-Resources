# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 下午4:16
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : views.py
# @Software: PyCharm

from flask import Blueprint

bp = Blueprint('cms', __name__, url_prefix='/cms', template_folder='pages')


@bp.route('/okc', methods=['GET', 'POST'])
def index():
    from flask import render_template
    from app.api.user.models import Gambler
    a = Gambler.query.filter_by(username=15013038819).first()
    print(a)
    # return 'okc.......'
    return render_template('test.html', a=a.username)

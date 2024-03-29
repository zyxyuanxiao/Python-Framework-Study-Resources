# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 上午9:38
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : views.py
# @Software: PyCharm

from flask import Blueprint, views, render_template, request, session, redirect, url_for, g, jsonify
from .forms import (
    LoginFrom,
    ResetpwdForm,
    ResetEmailForm,
    AddBannerForm,
    UpdateBannerForm,
    AddBoardForm,
    UpdateBoardForm, )

from .models import CMSUser, CMSPersmission
from ..models import BannerModel, BoardModel
from .decorators import login_required, permission_required
import config
from exts import db, mail
from flask_mail import Message
from utils import restful, zlcache
import string
import random
from apps.models import BannerModel
from tasks import send_mail

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/test')
@login_required
def test():
    return '1'


@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')


@bp.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('cms.login'))


@bp.route('/profile')
@login_required
def profile():
    return render_template('cms/cms_profile.html')


@bp.route('/email_captcha/')
def email_captcha():
    # /email_capthca/?email=xxx@qq.com
    email = request.args.get('email')
    if not email:
        return restful.params_error('请传递邮箱参数！')

    # 生成验证码
    source = list(string.ascii_letters)
    source.extend(map(lambda x: str(x), range(0, 10)))
    # source.extend(["0","1","2","3","4","5","6","7","8","9"])
    # captcha = random.sample(source, 6) # 合并list
    captcha = "".join(random.sample(source, 6))  # list转str

    # 发送

    # message = Message(
    #     '验证码',
    #     recipients=['yang6333yyx@126.com'],
    #     body='验证码: %s' % captcha)


    # try:
    #     mail.send(message)
    # except:
    #     return restful.server_error()
    # m = 'yang6333yyx@126.com'
    send_mail.delay('验证码', [email], '验证码: %s' % captcha)
    zlcache.set(email, captcha)
    return restful.success()


@bp.route('/posts/')
@login_required
@permission_required(CMSPersmission.POSTER)
def posts():
    return render_template('cms/cms_posts.html')


@bp.route('/comments/')
@login_required
@permission_required(CMSPersmission.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')


@bp.route('/boards/')
@login_required
@permission_required(CMSPersmission.BOARDER)
def boards():
    return render_template('cms/cms_boards.html')


@bp.route('/fusers/')
@login_required
@permission_required(CMSPersmission.FRONTUSER)
def fusers():
    return render_template('cms/cms_fusers.html')


@bp.route('/cusers/')
@login_required
@permission_required(CMSPersmission.CMSUSER)
def cusers():
    return render_template('cms/cms_cusers.html')


@bp.route('/croles/')
@login_required
@permission_required(CMSPersmission.ALL_PERMISSION)
def croles():
    return render_template('cms/cms_croles.html')


@bp.route('/banners/')
@login_required
def banners():
    banners = BannerModel.query.order_by(BannerModel.priority.desc()).all()
    return render_template('cms/cms_banners.html', banners=banners)


@bp.route('/abanner/', methods=['POST'])
@login_required
def abanner():
    form = AddBannerForm(request.form)
    if form.validate():
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data
        banner = BannerModel(name=name, image_url=image_url, link_url=link_url, priority=priority)
        db.session.add(banner)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/ubanner/', methods=['POST'])
@login_required
def ubanner():
    form = UpdateBannerForm(request.form)
    if form.validate():
        banner_id = form.banner_id.data
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data
        banner = BannerModel.query.get(banner_id)
        if banner:
            banner.name = name
            banner.image_url = image_url
            banner.link_url = link_url
            banner.priority = priority
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='没有这个轮播图！')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/dbanner/', methods=['POST'])
@login_required
def dbanner():
    banner_id = request.form.get('banner_id')
    if not banner_id:
        return restful.params_error(message='请传入轮播图id！')

    banner = BannerModel.query.get(banner_id)
    if not banner:
        return restful.params_error(message='没有这个轮播图！')

    db.session.delete(banner)
    db.session.commit()
    return restful.success()


# 登录
class LoginView(views.MethodView):
    def get(self, message=None):
        return render_template('cms/cms_login.html', message=message)

    def post(self):
        form = LoginFrom(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='邮箱或者密码错误')
        else:
            print(form.errors)
            message = '输入格式有误'
            return self.get(message=message)


# 改密码
class ResetPwdView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        form = ResetpwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                # {"code":200,message=""}
                # return jsonify({"code":200,"message":""})
                return restful.success()
            else:
                return restful.params_error("旧密码错误！")
        else:
            return restful.params_error(form.get_error())


# 改邮箱
class ResetEmailView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetemail.html')

    def post(self):
        form = ResetEmailForm(request.form)
        if form.validate():
            email = form.email.data
            g.cms_user.email = email
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(form.get_error())


bp.add_url_rule('/login', view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd', view_func=ResetPwdView.as_view('resetpwd'))
bp.add_url_rule('/resetemail', view_func=ResetEmailView.as_view('resetemail'))

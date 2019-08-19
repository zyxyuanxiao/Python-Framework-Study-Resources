#!/usr/bin/env python
# encoding: utf-8

from app import app, login_manager
from exts import db
from app.models import Match, Gambler, Monitor, Article, Push, Profile
from flask_login import login_user, logout_user, current_user, login_required
from flask import session, g, request
from ctrl_func.ApiResult import *
from ctrl_func.re_tel import *
from ctrl_func.model_class_serialize import *
import datetime
from app.app_decorators import app_vip_decorator
import time

now_time = datetime.datetime.now()

'''_____________________________________________________________'''


# 拦截调试
@app.route('/test', methods=['GET'])
@login_required
def test():
    return ApiResult().formattingData(status=200, msg='调试通过', data=[])


@app.route('/lien')
def lien():
    return ApiResult().formattingData(status=403, msg='未登录', data=[])


# flask-login
@login_manager.user_loader
def load_user(gambler_id):
    return Gambler.query.get(gambler_id)


@app.before_request
def before_request():
    g.gambler = current_user


# @login_manager.unauthorized_handler
# def unauthorized_handler():
#     return redirect(url_for('lien'))


@app.context_processor
def my_context_processor():
    gambler_id = session.get('gambler_id')
    if gambler_id:
        gambler = Gambler.query.filter(Gambler.id == gambler_id).first()
        return {'gambler': gambler}
    return {}


'''_____________________________________________________________app登录-注册-退出'''


# app注册
@app.route('/register', methods=['POST'])
def app_register():
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    nickname = '老铁取个昵称吧'
    level = 1

    gambler = Gambler.query.filter_by(username=username).first()

    if gambler:
        return ApiResult().formattingData(status=0, msg='用户名已经被注册!', data=[])

    if username == '':
        return ApiResult().formattingData(status=1, msg='手机号不能为空!', data=[])

    if len(username) < 11 or len(username) > 11:
        return ApiResult().formattingData(status=2, msg='手机号长度应11位数字!', data=[])

    if not tels(username):
        return ApiResult().formattingData(status=2, msg='手机号格式不正确!', data=[])

    if password == '':
        return ApiResult().formattingData(status=3, msg='密码不能为空!', data=[])

    if password != password2:
        return ApiResult().formattingData(status=4, msg='两次输入的密码不一致!', data=[])

    if len(password) < 6 or len(password) > 14:
        return ApiResult().formattingData(status=5, msg='密码少于6位或多于14!', data=[])

    gambler = Gambler(username, password, nickname, level)
    db.session.add(gambler)
    db.session.commit()
    gg = gambler.id
    profile = Profile(nkname='老铁取个昵称吧', tel='手机号？', u_id=gg)
    db.session.add(profile)
    db.session.commit()

    return ApiResult().formattingData(status=200, msg='注册成功!', data={
        "app_id": gambler.id,
        "mobile": '',
        "mobile_encode": '',
        "app_levle": gambler.level,
        "last_login_ip": '',
        "login_time": '',
        "nickname": '',
        'username': '',

        "avatar_original": {
            "life_time": '',
            "login_encode": 'login_encode',
        },

        "api_token": {"life_time": 'life_time',
                      },
    })


# app登陆
@app.route('/login', methods=['POST'])
def app_login():
    username = request.form.get('username')
    password = request.form.get('password')
    gambler = Gambler.query.filter_by(username=username).first()
    # p = True

    if not gambler:
        return ApiResult().formattingData(status=-1, msg='手机号未注册', data={})

    if username == '':
        return ApiResult().formattingData(status=-2, msg='用户名-不能为空', data={})

    p = gambler.check_passwodr(password)

    if password == '':
        return ApiResult().formattingData(status=-3, msg='密码-不能为空', data={})

    if not p:
        return ApiResult().formattingData(status=-4, msg='密码-错误', data={})

    # session['gambler_id'] = gambler.id
    session.permanent = True
    login_user(user=gambler)

    u = Monitor(mobile=username)
    # print('>>', u)

    # m = hashlib.md5()
    # m.update(username.encode(encoding="utf-8"))
    # m.update(password.encode(encoding="utf-8"))
    # m.update(str(int(time.time())).encode(encoding="utf-8"))
    # token = m.hexdigest()
    # print(token)
    #
    # r.hmset('user:%s' % user.mobile, {'token': token,
    #                                   'nickname': user.username,
    #                                   'app_online': 1})
    # r.set('token:%s' % token, user.mobile)
    # r.expire('token:%s' % token, 3600 * 24 * 30)

    # tk = session.pop('api_token', None)
    # if tk == None:
    #     return ApiResult().formattingData(status=-1, msg='none!', data=[])
    #
    # api_token = request.form.get('api_token')
    # if api_token != tk:
    #     return ApiResult().formattingData(status=0, msg='ok!', data=[])
    #
    # tk = str(uuid.uuid1())
    # r.set('login-' + mobile, tk, ex=3600 * 24 * 30)
    # r.set('login-' + mobile, tk, ex=30)

    m = Monitor.query.filter_by(mobile=username).first()
    if not m:
        m1 = Monitor(username)
        db.session.add(m1)
        db.session.commit()
    else:
        m2 = Monitor(mobile=request.form.get('username'))
        db.session.add(m2)
        db.session.commit()
    return ApiResult().formattingData(status=200, msg='登录成功', data={
        'app_id': gambler.id,
        'mobile': gambler.username,
        'app_levle': gambler.level,
        'last_login_time': '',
        'login_time': now_time,
        'nickname': gambler.nickname,
        'token': '',
        'login_encode': {
            'life_time': '',
            'login_encode': '',
        }
    })


# app退出
@app.route('/logout', methods=['GET'])
@login_required
def app_logout():
    session.clear()
    logout_user()
    return ApiResult().formattingData(status=200, msg='退出成功', data=[])


'''_____________________________________________________________app首页'''


# app首页-比赛列表
@app.route('/app_index', methods=['GET'])
# @login_required
def app_index():
    # app_index?pageIndex=1&pageSize=5
    arr = []
    page = request.args.get('pageIndex', 1, type=int)
    size = request.args.get('pageSize')
    # print('当前页', page, '当前条数', size)
    pagination = Match.query.order_by('cea_time').paginate(page, per_page=int(size), error_out=False)
    # print(pagination)
    p = pagination.items
    # print('当前列表', p)
    t = pagination.total
    for i in p:
        arr.append(row2dict(i))
    return ApiResult().formattingData(status=200, msg='index', data={
        'records': arr,
        'now_page': page,
        'totalAmount': t

    })


'''_____________________________________________________________app文章'''


# app原创文章(免费)
@app.route('/app_article', methods=['GET'])
@login_required
def article():
    m = Article.query.order_by(-Article.cea_time).filter(Article.al == 1, Article.state == 1).all()
    arr = []
    for i in m:
        a = row2dict(i)
        arr.append(a)
    return ApiResult().formattingData(status=200, msg='原创文章', data=arr)


# app原创文章内页
@app.route('/app_article<article_id>', methods=['GET'])
@login_required
def article_ny(article_id):
    m = Article.query.filter(Article.id == article_id, Article.al == 1).first()
    if m:
        arr = []
        a = row2dict(m)
        arr.append(a)
        return ApiResult().formattingData(status=200, msg='原创文章', data=arr)
    else:
        return ApiResult().formattingData(status=404, msg='未找到该文章', data=[])


# app转载文章(免费)
@app.route('/app_article_2', methods=['GET'])
@login_required
def r_article():
    m = Article.query.order_by(-Article.cea_time).filter(Article.al == 2, Article.state == 1).all()
    arr = []
    for i in m:
        a = row2dict(i)
        arr.append(a)
    return ApiResult().formattingData(status=200, msg='转载文章', data=arr)


# app转载文章内页
@app.route('/app_article_2<article_id>', methods=['GET'])
@login_required
def r_article_ny(article_id):
    m = Article.query.filter(Article.id == article_id, Article.al == 2).first()
    if m:
        arr = []
        a = row2dict(m)
        arr.append(a)
        return ApiResult().formattingData(status=200, msg='转载文章', data=arr)
    else:
        return ApiResult().formattingData(status=404, msg='未找到该文章', data=[])


'''_____________________________________________________________app比赛推荐'''


# app【免费】推荐
@app.route('/app_push', methods=['GET'])
@login_required
def app_push():
    v = Push.query.order_by(-Push.cea_time).filter(Push.cost == 1).all()
    arr = []
    for i in v:
        a = row2dict(i)
        arr.append(a)
    return ApiResult().formattingData(status=200, msg='免费推荐', data=arr)


# app【免费】推荐内页
@app.route('/app_push_ny<push_id>', methods=['GET'])
def app_push_ny(push_id):
    m = Push.query.filter(Push.id == push_id, Push.cost == 1).first()
    if m:
        arr = []
        a = row2dict(m)
        arr.append(a)
        return ApiResult().formattingData(status=200, msg='免费推荐', data=arr)
    else:
        return ApiResult().formattingData(status=404, msg='未找到该推荐信息', data=[])


# app【收费】推荐显示列表
@app.route('/app_push_pay', methods=['GET'])
@login_required
def app_push_pay():
    arr = []
    v = Push.query.order_by(-Push.cea_time).filter(Push.cost == 2).all()
    # i = Gambler.query.filter(Gambler.id == g.gambler.id).first()
    # if i.level != '2':
    #     return ApiResult().formattingData(status=1, msg='普通用户', data=[
    #         {
    #             'id': i.id,
    #             'level': i.level
    #         }])
    for i in v:
        a = row2dict(i)
        arr.append(a)
    return ApiResult().formattingData(status=2, msg='会员用户', data=arr)


# app【收费】推荐内页
@app.route('/app_push_pay_ny<push_id>', methods=['GET'])
@login_required
@app_vip_decorator
def app_push_pay_ny(push_id):
    m = Push.query.filter(Push.id == push_id, Push.cost == 2).first()
    if not m:
        return ApiResult().formattingData(status=404, msg='未找到对应的推荐内页', data=[])

    i = Gambler.query.filter(Gambler.id == g.gambler.id).first()
    if i.level != '2':
        return ApiResult().formattingData(status=1, msg='普通用户', data=[
            {
                'id': i.id,
                'level': i.level
            }])
    if m:
        arr = []
        a = row2dict(m)
        arr.append(a)
        return ApiResult().formattingData(status=2, msg='会员用户', data=arr)
    else:
        return ApiResult().formattingData(status=1, msg='普通用户', data=[])


'''_________________________________________________________________app合作/个人资料'''


# app合作
@app.route('/app_coop', methods=['GET'])
def app_coop():
    return ApiResult().formattingData(status=200, msg='合作', data={})


# 个人资料profile
@app.route('/app_profile<gambler_id>', methods=['GET', 'POST'])
@login_required
def app_profile(gambler_id):
    u = Gambler.query.filter(Gambler.id == gambler_id).first()
    p = Profile.query.filter(Profile.u_id == gambler_id).first()
    if not u:
        return ApiResult().formattingData(status=404, msg='该用户不存在的！！！', data=[])
    elif p:
        return ApiResult().formattingData(status=200, msg='个人资料', data={
            'id': u.id,
            'nickename': u.nickname,
            'tel': p.tel,
            'level': u.level})


# 修改个人资料
@app.route('/app_profile_modify<gambler_id>', methods=['GET', 'POST'])
@login_required
def app_profile_modify(gambler_id):
    n = request.form.get('nickname')
    u = Gambler.query.filter(Gambler.id == gambler_id).first()
    if not u:
        return ApiResult().formattingData(status=404, msg='该用户不存在的！！！', data=[])
    elif n:
        # Gambler.query.filter(Gambler.id == gambler_id).update({'level': '2'})
        Gambler.query.filter(Gambler.id == gambler_id).update({'nickname': n})
        db.session.commit()
        return ApiResult().formattingData(status=200, msg='修改成功', data=[])
    else:
        return ApiResult().formattingData(status=200, msg='未进行修改', data=[])

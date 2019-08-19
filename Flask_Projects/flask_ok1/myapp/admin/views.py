#!/usr/bin/env python
# encoding: utf-8
from flask import render_template, request, session, redirect, url_for, g
from exts import db
from myapp import photos
from . import admin
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import or_
from myapp.models import User, House, Match, Article
import uuid
import datetime
from functools import wraps

now_time = datetime.datetime.now()

'''_____________________第一部分______________________________'''


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin():
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)

    return decorated_function


#
# # flask-login
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)


@admin.before_request
def before_request():
    g.user = current_user


@admin.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        return {'user': user}
    return {}


# token
@admin.route('/token', methods=['GET'])
def get_token():
    api_token = str(uuid.uuid1())
    session['api_token'] = api_token
    return api_token


# 404页
@admin.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


'''_____________________第二部分______________________________'''


# 调试
@admin.route('/okc', methods=['GET'])
def okc():
    return render_template('form_validation.html')
    # return 'ok_>>>>>>>'


'''_____________________第三部分______________________________'''


# 首页
@admin.route('/', methods=['GET'])
def home_page():
    if g.user:
        return redirect(url_for('admin.index'))
    return render_template('login.html')


# 登录验证
@admin.route('/index', methods=['GET'])
@login_required
@admin_required
def index():
    return render_template('index.html', u=g.user.username)


'''_____________________第四部分______________________________'''


# 注册
@admin.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('login.html')

    else:
        nickname = request.form.get('nickname')
        address = request.form.get('address')
        city = request.form.get('city')
        country = request.form.get('country')
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if nickname == '':
            return '昵称。。。'
        if address == '':
            return '地区。。。'
        if city == '':
            return '城市。。。'
        if country == '':
            return '国家。。。'

        user = User.query.filter(User.username == username).first()
        # if user == None:
        #     return '用户名。。。'
        if user:
            return '用户名已经存在'
        elif password != password2:
            return '两次密码不一致'
        else:
            user = User(nickname=nickname,
                        address=address,
                        city=city,
                        country=country,
                        username=username,
                        password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('admin.index'))


# 登录
@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        # print(user)

        if username == '':
            return '用户名-不能唯空'
        if password == '':
            return '密码-不能唯空'
        if not user:
            return '用户名-未注册'

        p = user.check_passwodr(password)
        # print(p)

        if not p:
            return '密码-错误'

    if user and p:
        # session['user_id'] = user.id
        session.permanent = True
        login_user(user)
        return redirect(url_for('admin.index'))


# 注销
@admin.route('/logout', methods=['GET'])
def logout():
    # session 关闭浏览器后清除
    # session.pop('user_id)
    # del session['user_id']
    session.clear()
    # 不清除
    logout_user()
    return redirect(url_for('admin.home_page'))


'''_____________________第五部分______________________________'''


# 信息
@admin.route('/h_add', methods=['GET'])
@login_required
def h_add():
    return render_template('list.html', u=g.user.username)


# 提交
@admin.route('/sub', methods=['POST'])
@login_required
def h_sub():
    if request.method == 'POST' and 'photo' in request.files:
        # if 'file' not in request.files:
        #     flash('用户没有提交文件')
        try:
            f = request.files['photo']
            print(f)
            print(type(f))
            filename = photos.save(f)
            print(type(filename))
            file_url = photos.url(filename)
            title = request.form.get('title')
            region = request.form.get('region')
            price = request.form.get('price')
            households = request.form.get('households')
            describe = request.form.get('describe')
            u = g.user.id
            if title == '':
                return '标题xx'
            if region == '':
                return '区域xx'
            if price == '':
                return '售价xx'
            if households == '':
                return '面积xx'
        except BaseException as e:
            return '图片为空或名称为中文'

        house = House(title=title,
                      region=region,
                      price=price,
                      households=households,
                      describe=describe,
                      auth_id=u,
                      image_name=filename,
                      image_path=file_url)
        db.session.add(house)
        db.session.commit()

        return render_template('list.html')


# 信息列表
@admin.route('/h_mess_list2', methods=['GET'])
@login_required
def h_mess_list2():
    # 分页
    # 从request的参数中获取参数page的值
    # 如果参数不存在那么返回默认值1
    # type=int保证返回的默认值是整形数字
    page = request.args.get('page', 1, type=int)
    # 第一个参数表示要查询的页数
    # 第二个参数是每页显示的数量,如果不设置默认显示20条
    # 第三个参数如果设置成:True，当请求的页数超过了总的页数范围，就会返回一个404错误
    #  如果设为:False，就会返回一个空列表。
    pagination = House.query.order_by('-release_time').paginate(page, per_page=3, error_out=False)
    context = {
        'h_lists': pagination.items
    }
    return render_template('h_mess_list2.html', **context, pagination=pagination, u=g.user.username)


# 信息详情
@admin.route('/detail<h_id>', methods=['GET'])
@login_required
def detail(h_id):
    context = {
        'h_det': House.query.filter(House.id == h_id).first()
    }
    return render_template('h_mess_list.html', **context)


# 信息查询
@admin.route('/search/', methods=['GET'])
@login_required
def search():
    q = request.args.get('q')
    page = request.args.get('page', 1, type=int)
    # 标题和内容包含关键字
    pagination = House.query.filter(or_(House.title.like('%' + q + '%') if q is not None else '',
                                        House.describe.like('%' + q + '%') if q is not None else '')
                                    ).order_by('-release_time').paginate(page, per_page=5, error_out=False)
    context = {
        'h_lists': pagination.items
    }
    return render_template('h_mess_list2.html', **context, pagination=pagination)


# 分页
@admin.route('/pages', methods=['GET'])
def pages():
    page = request.args.get('page', 1, type=int)
    pagination = House.query.order_by('-release_time').paginate(page, per_page=5, error_out=False)
    h_lists = pagination.items
    return render_template('h_mess_list2.html', h_lists=h_lists, pagination=pagination)


# 个人资料
@admin.route('/user_pf', methods=['GET'])
@login_required
def user_pf():
    return render_template('page_user_profile_1_account.html', u=g.user.username)


'''_____________________比赛______________________________'''


# 1.比赛信息页
@admin.route('/vs_add', methods=['GET'])
@login_required
def vs_add():
    return render_template('vs_mess_add.html', u=g.user.username)


# 2.比赛信息添加
@admin.route('/vs_sub', methods=['POST'])
@login_required
def vs_sub():
    if request.method == 'POST':
        vs_type = request.form.get('vs_type')
        vs = request.form.get('vs')
        vs_code = request.form.get('vs_code')
        vs_time = request.form.get('vs_time')
        victory = request.form.get('victory')
        ping = request.form.get('ping')
        fail = request.form.get('fail')
        victory_code = request.form.get('victory_code')
        ping_code = request.form.get('ping_code')
        fail_code = request.form.get('fail_code')
        let_ball = request.form.get('let_ball')
        if vs_type == '':
            return '标题xx'
        if vs == '':
            return '区域xx'
        if vs_code == '':
            return '售价xx'
        if vs_time == '':
            return '面积xx'
        if victory == '':
            return '标题xx'
        if ping == '':
            return '区域xx'
        if fail == '':
            return '售价xx'
        if victory_code == '':
            return '面积xx'
        if ping_code == '':
            return '面积xx'
        if fail_code == '':
            return '面积xx'
        if let_ball == '':
            return '面积xx'

        match = Match(vs_type=vs_type,
                      vs=vs,
                      vs_code=vs_code,
                      vs_time=vs_time,
                      victory=victory,
                      ping=ping,
                      fail=fail,
                      victory_code=victory_code,
                      ping_code=ping_code,
                      fail_code=fail_code,
                      let_ball=let_ball, )
        db.session.add(match)
        db.session.commit()

        return render_template('vs_mess_add.html')


# 3.比赛信息_lists_显示
@admin.route('/vs_list', methods=['GET'])
@login_required
def vs_list():
    page = request.args.get('page', 1, type=int)
    pagination = Match.query.order_by('-cea_time').paginate(page, per_page=3, error_out=False)
    context = {
        'vs_lists': pagination.items
    }
    return render_template('vs_mess_list.html', **context, pagination=pagination, u=g.user.username)


# 4.比赛信息详情内页
@admin.route('/vs_list_ny<h_id>', methods=['GET'])
@login_required
def vs_list_ny(h_id):
    context = {
        'h_det': Match.query.filter(Match.id == h_id).first()
    }
    return render_template('vs_mess_list_ny.html', **context)


# 5.删除比赛消息
@admin.route('/vs_list_del<h_id>', methods=['GET'])
@login_required
def vs_list_del(h_id):
    dm = Match.query.filter(Match.id == h_id).first()
    print(dm)
    db.session.delete(dm)
    db.session.commit()
    return redirect(url_for('admin.vs_list'))


# 6.比赛信息查询
@admin.route('/vs_search/', methods=['GET'])
@login_required
def vs_search():
    q = request.args.get('q')
    page = request.args.get('page', 1, type=int)
    # 标题和内容包含关键字
    pagination = Match.query.filter(or_(Match.vs_type.like('%' + q + '%') if q is not None else '',
                                        Match.vs_code.like('%' + q + '%') if q is not None else '')
                                    ).order_by('-cea_time').paginate(page, per_page=5, error_out=False)
    context = {
        'vs_lists': pagination.items
    }
    return render_template('vs_mess_list.html', **context, pagination=pagination)


'''_____________________文章______________________________'''


# 7.文章添加页面
@admin.route('/add_article', methods=['GET', 'POST'])
@login_required
def add_article():
    return render_template('vs_article_add.html', u=g.user.username)


# 8.文章添加
@admin.route('/vs_article_sub', methods=['GET', 'POST'])
@login_required
def vs_article_sub():
    if request.method == 'POST' or 'photo' in request.files:

        title = request.form.get('title')
        author = request.form.get('author')
        vs_category = request.form.get('vs_category')
        vs_other_c = request.form.get('vs_other_c')
        vs = request.form.get('vs')
        al = request.form.get('al')
        link = request.form.get('link')
        content = request.form.get('content')
        vs_push = request.form.get('vs_push')
        state = request.form.get('state')
        if title == '':
            return '标题?'
        if author == '':
            return '作者?'
        if vs == '':
            return '对阵？'
        if not al:
            return '文章类别?'
        if content == '':
            return '内容?'
        f = request.files['photo']
        if f:
            filename = photos.save(f)
            file_url = photos.url(filename)
        else:
            filename = ''
            file_url = ''

        art = Article(title=title,
                      author=author,
                      vs_category=vs_category,
                      vs_other_c=vs_other_c,
                      vs=vs,
                      al=al,
                      link=link,
                      content=content,
                      vs_push=vs_push,
                      state=state,
                      image_name=filename,
                      image_path=file_url)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for('admin.add_article'))


# 9.文章列表
@admin.route('/vs_article', methods=['GET'])
@login_required
def vs_article():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by('-cea_time').paginate(page, per_page=3, error_out=False)
    context = {
        'vs_article_lists': pagination.items
    }
    return render_template('vs_article_list.html', **context, pagination=pagination, u=g.user.username)


# 10.文章详情内页
@admin.route('/vs_article_ny<h_id>', methods=['GET'])
@login_required
def vs_article_ny(h_id):
    context = {
        'h_det': Article.query.filter(Article.id == h_id).first()
    }
    return render_template('vs_article_ny.html', **context)


# 11.文章查询
@admin.route('/vs_article_search/', methods=['GET'])
@login_required
def vs_article_search():
    q = request.args.get('q')
    page = request.args.get('page', 1, type=int)
    # 标题和内容包含关键字
    pagination = Article.query.filter(or_(Article.title.like('%' + q + '%') if q is not None else '',
                                          Article.vs.like('%' + q + '%') if q is not None else '')
                                      ).order_by('-cea_time').paginate(page, per_page=5, error_out=False)
    context = {
        'vs_article_lists': pagination.items
    }
    return render_template('vs_article_list.html', **context, pagination=pagination)


# 12.删除文章
@admin.route('/vs_article_del<h_id>', methods=['GET'])
@login_required
def vs_article_del(h_id):
    dm = Article.query.filter(Article.id == h_id).first()
    print(dm)
    db.session.delete(dm)
    db.session.commit()
    return redirect(url_for('admin.vs_article'))

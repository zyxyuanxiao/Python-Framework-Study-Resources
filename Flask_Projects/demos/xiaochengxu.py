from flask import Flask, views, jsonify, redirect, url_for, request
from functools import wraps

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        u = request.args.get('u')
        if u == 'y':
            return func(*args, **kwargs)
        else:
            return '未登录'

    return wrapper


class JsonView(views.View):
    def get_data(self):
        raise NotImplemented

    def dispatch_request(self):
        return jsonify(self.get_data())


class ListView(JsonView):
    def get_data(self):
        return {
            'user': 'y',
            'pwd': '1',
        }


# endpoint:代替函数名称，view_func=ListView.as_view('list'):取名
app.add_url_rule('/list', endpoint='yyx', view_func=ListView.as_view('list'))


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/x')
def my_list():
    # print(url_for('yyx'))
    # return 'list'
    return redirect(url_for('yyx'))


class LoginView(views.MethodView):
    decorators = [login_required]

    def _func(self):
        pass

    def get(self):
        return '1'

    def post(self):
        return '2'


app.add_url_rule('/login', view_func=LoginView.as_view('login'))

if __name__ == '__main__':
    app.run()

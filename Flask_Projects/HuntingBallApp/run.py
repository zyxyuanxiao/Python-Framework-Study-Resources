# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 下午3:55
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : run.py
# @Software: PyCharm

from app import create_app
import os

print('FLASK_ENV: %s' % os.environ.get('FLASK_ENV'))


def main():
    app = create_app()
    app.run(host=app.config['RUN_HOST'], port=app.config['RUN_PORT'])
    # app.run()


if __name__ == '__main__':
    main()
    # app = create_app()
    # app.run(host=app.config['RUN_HOST'], port=app.config['RUN_PORT'])

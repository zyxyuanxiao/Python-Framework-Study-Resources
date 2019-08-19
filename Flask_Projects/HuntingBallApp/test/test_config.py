# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 下午2:02
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_config.py
# @Software: PyCharm

import os

config_key = 'development'
if os.environ.get('FLASK_ENV') == 'development':
    config_key = 'development'
    print('开发环境', config_key)
elif os.environ.get('FLASK_ENV') == 'production':
    config_key = 'production'
    print('生产环境', config_key)
else:
    config_key = 'default'
    print('Pycharm开发环境', config_key)

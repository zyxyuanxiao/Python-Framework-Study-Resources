# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 下午3:56
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : service.py
# @Software: PyCharm

from .models import Match
from utils.apiResult import ex_er
from utils.tool import row2dict


class MatchService(object):
    @staticmethod
    def add_match(data):

        for i, j in data.items():
            if data[i] == '':
                ex_er(1005)

        m = Match()
        m.vs_type = data.get('vs_type')
        m.home_team = data.get('home_team')
        m.visiting_team = data.get('visiting_team')
        m.vs_code = data.get('vs_code')
        m.vs_time = data.get('vs_time')
        m.victory = data.get('victory')
        m.ping = data.get('ping')
        m.fail = data.get('fail')
        m.victory_code = data.get('victory_code')
        m.ping_code = data.get('ping_code')
        m.fail_code = data.get('fail_code')
        m.let_ball = data.get('let_ball')
        return m

    @staticmethod
    def read(data):
        arr = []
        # import time
        # import datetime
        # now_day = datetime.datetime.now().strftime('%Y-%m-%d')
        # print('当前日期', now_day, type(now_day))
        #
        # now_time = datetime.datetime.now()
        # print('当前时间', now_time, type(now_time))
        #
        # zz = time.mktime(now_time.timetuple())
        # print('当前时间戳', zz, type(zz))
        #
        # onlie = Match.query.filter(Match.vs_time < now_day).all()  # 当日前
        # print('matchs', onlie)
        #
        # for j in onlie:
        #     print(j.id)
        #     print(j.vs_time, type(j.vs_time))
        #     print(j.status)

        # ?pageIndex=1&pageSize=5
        # page = request.args.get('pageIndex', 1, type=int)
        # size = request.args.get('pageSize')
        # print('当前页', page, '当前条数', size)

        page = int(data['pageIndex'])
        size = int(data['pageSize'])
        pagination = Match.query.filter_by(status='1').order_by('cea_time').paginate(page, per_page=int(size),
                                                                                     error_out=False)
        # print(pagination)

        p = pagination.items
        # print('当前列表', p)

        t = pagination.total
        for i in p:
            arr.append(row2dict(i))
        d = {
            'records': arr,
            'now_page': page,
            'totalAmount': t
        }
        return d

    @classmethod
    def up_match(cls, data):
        cls.add_match(data=data)
        # print('service', data['id'])
        # print('service', cls.add_match(data=data))
        match_id = data['id']
        m = Match.query.filter_by(id=match_id).first()
        m.vs_type = cls.add_match(data=data).vs_type
        m.home_team = cls.add_match(data=data).home_team
        m.visiting_team = cls.add_match(data=data).visiting_team
        m.vs_code = cls.add_match(data=data).vs_code
        m.vs_time = cls.add_match(data=data).vs_time
        m.victory = cls.add_match(data=data).victory
        m.ping = cls.add_match(data=data).ping
        m.fail = cls.add_match(data=data).fail
        m.victory_code = cls.add_match(data=data).victory_code
        m.ping_code = cls.add_match(data=data).ping_code
        m.fail_code = cls.add_match(data=data).fail_code
        m.let_ball = cls.add_match(data=data).let_ball
        return m

    @staticmethod
    def del_match(data):
        for i, j in data.items():
            if data[i] == '':
                ex_er(400)
        m = Match.query.filter_by(id=data['id']).first()
        m.status = data['status']
        return m

# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 下午3:13
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : models.py
# @Software: PyCharm

from exts import db
import enum
from datetime import datetime
import datetime


class MatchEnum(enum.Enum):
    Normal = '1'
    Deleted = '2'
    Abnormal = '3'


# 比赛场次信息
class Match(db.Model):
    __tablename__ = 'match'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vs_type = db.Column(db.String(128), nullable=False)  # 联赛类型
    home_team = db.Column(db.String(128), nullable=False)  # 主队
    visiting_team = db.Column(db.String(128), nullable=False)  # 客队
    # vs = db.Column(db.String(128), nullable=False)
    vs_code = db.Column(db.String(128), nullable=False)  # 场次编号
    vs_time = db.Column(db.String(128), nullable=False)  # 比赛时间
    victory = db.Column(db.String(128), nullable=False)  # 胜
    ping = db.Column(db.String(128), nullable=False)  # 平
    fail = db.Column(db.String(128), nullable=False)  # 负
    victory_code = db.Column(db.String(128), nullable=False)  # 让球-胜
    ping_code = db.Column(db.String(128), nullable=False)  # 让球-平
    fail_code = db.Column(db.String(128), nullable=False)  # 让球-负
    let_ball = db.Column(db.String(128), nullable=False)  # 主队让(受)球数
    # status = db.Column(db.Enum(MatchEnum), default=MatchEnum.Normal)
    status = db.Column(db.String(128), default='1')
    cea_time = db.Column(db.DateTime, server_default=db.func.now())

    # def __init__(
    #         self, vs_type, home_team, visiting_team, vs_code, vs_time, victory, ping, fail, victory_code, ping_code,
    #         fail_code, let_ball
    # ):
    #     self.vs_type = vs_type
    #     self.home_team = home_team
    #     self.visiting_team = visiting_team
    #     self.vs_code = vs_code
    #     self.vs_time = vs_time
    #     self.victory = victory
    #     self.ping = ping
    #     self.fail = fail
    #     self.victory_code = victory_code
    #     self.ping_code = ping_code
    #     self.fail_code = fail_code
    #     self.let_ball = let_ball

    def to_dict(self):
        match_dict = {}
        match_dict['id'] = self.id
        match_dict['vs_type'] = self.vs_type
        match_dict['home_team'] = self.home_team
        match_dict['visiting_team'] = self.visiting_team
        match_dict['vs_code'] = self.vs_code
        match_dict['vs_time'] = self.vs_time
        match_dict['victory'] = self.victory
        match_dict['ping'] = self.ping
        match_dict['fail'] = self.fail
        match_dict['victory_code'] = self.victory_code
        match_dict['ping_code'] = self.ping_code
        match_dict['fail_code'] = self.fail_code
        match_dict['let_ball'] = self.let_ball
        match_dict['cea_time'] = self.cea_time.strftime('%Y-%m-%d %H:%M:%S')
        # match_dict['status'] = Match.status

        return match_dict

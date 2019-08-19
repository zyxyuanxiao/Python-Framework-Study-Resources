#!/usr/bin/env python
# encoding: utf-8
from flask import jsonify


class ApiResult(object):
    def formattingData(self, status, msg, data):
        return jsonify(
            {
                "status": status,
                "msg": msg,
                "data": data
            }
        )

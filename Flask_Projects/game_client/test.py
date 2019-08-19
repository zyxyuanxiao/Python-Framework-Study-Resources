#!/usr/bin/env python
# encoding: utf-8

from exts import db
from app.models import Gambler
from flask import g

g = Gambler(password=g.gambler.password, level=2)
db.session.add(g)
db.session.commit()

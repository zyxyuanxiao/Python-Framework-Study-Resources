# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import pytest
from webtest import TestApp

from flask_server.app import create_app
from flask_server.ext import db as _db
from flask_server.config import TestConfig

from .factories import UserFactory, ArticleFactory, ModuleFactory


@pytest.fixture
def app():
    """An application for the tests."""
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def testapp(app):
    """A Webtest app."""
    return TestApp(app)


@pytest.fixture
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def user(db):
    """A user for the tests."""
    user = UserFactory(username='test123', password='test123')
    db.session.commit()
    return user


@pytest.fixture
def get_token(testapp):
    user = UserFactory(username='test123', password='test123')
    user.save()
    res = testapp.post_json('/admin/login', {'username': 'test123', 'password': 'test123'})
    return dict(Authorization=res.json['data']['token'])


@pytest.fixture
def article(db):
    """An article for the tests."""
    article = ArticleFactory(title='sadsadasdastestss', content='shshhahhahs')
    db.session.commit()
    return article

@pytest.fixture
def module(db):
    """A module for the tests."""
    module = ModuleFactory(title='sadsadasdastestss')
    db.session.commit()
    return module
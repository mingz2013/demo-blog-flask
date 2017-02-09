# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint

main = Blueprint('main', __name__, url_prefix='')

from . import articles, errors

from app.database import db_session


@main.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

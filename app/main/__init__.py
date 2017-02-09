# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint

main = Blueprint('main', __name__, url_prefix='')

from . import articles, errors



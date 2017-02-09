# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from datetime import datetime
from flask import render_template, session, redirect, url_for, request

from . import main
from .. import db
from ..models import Article, Comment


@main.route('/', methods=['GET'])
@main.route('/<int:page>', methods=['GET'])
def index(page=0):
    return render_template('articles/index.html', articles=[])


@main.route('/article/<int:id>', methods=['GET'])
def article(id):
    article = None
    return render_template('articles/detail.html', article=article)


@main.route('/article/post', methods=['GET', 'POST'])
def post():
    id = request.args.get('id', '')
    if id:
        # post = Article.query.get_or_404(id)
        article = None
        return render_template('articles/edit.html', article=article)
    else:
        return render_template('articles/new.html')

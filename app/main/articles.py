# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from datetime import datetime
from flask import render_template, session, redirect, url_for, request

from . import main
from .. import db
from ..models import Article, Comment


@main.route('/', methods=['GET'])
@main.route('/<int:page>', methods=['GET'])
def index(page=None):
    return render_template('articles/index.html', articles=[])


@main.route('/article/<int:id>', methods=['GET'])
def article(id):
    article = None
    return render_template('articles/detail.html', article=article)


@main.route('/article/post', methods=['GET', 'POST'])
def post():
    id = request.args.id
    post = Article.query.get_or_404(id)
    return render_template('post.html', posts=[post])

# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import render_template, redirect, url_for, request

from app import db
from . import main
from ..models import Article


@main.route('/', methods=['GET'])
@main.route('/<int:page>', methods=['GET'])
def index(page=0):
    articles = Article.query.all()
    return render_template('articles/index.html', articles=articles)


@main.route('/article/<int:id>', methods=['GET'])
def article(id):
    article = Article.query.filter_by(id=id).first()
    return render_template('articles/detail.html', article=article)


@main.route('/article/post', methods=['GET', 'POST'])
def post():
    if request.method == "GET":
        id = request.args.get('id', '')
        if id:
            article = Article.query.filter_by(id=id).first()
            return render_template('articles/edit.html', article=article)
        else:
            return render_template('articles/new.html')
    else:
        title = request.form.get('title', '')
        content = request.form.get('content', '')
        id = 0
        article = Article(title=title, content=content, id=id)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('main.article', id=id))

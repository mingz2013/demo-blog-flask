# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import render_template, redirect, url_for, request

from app import db
from . import main
from ..models import Article, Comment
from app.dbredis import RedisClient


@main.route('/', methods=['GET'])
@main.route('/<int:page>', methods=['GET'])
def index(page=1):
    pagination = Article.query.order_by(Article.create_at.desc()).paginate(page, per_page=10, error_out=False)
    articles = pagination.items
    print articles
    return render_template('articles/index.html', articles=articles, pagination=pagination)


@main.route('/article/<int:id>', methods=['GET'])
def article(id):
    article = Article.query.filter_by(id=id).first()
    comments = Comment.query.filter_by(article_id=id)
    return render_template('articles/detail.html', article=article, comments=comments)


@main.route('/article/post', methods=['GET', 'POST'])
def post():
    id = request.args.get('id', '')
    if request.method == "GET":
        if id:
            article = Article.query.filter_by(id=id).first()
            return render_template('articles/edit.html', article=article)
        else:
            return render_template('articles/new.html')
    else:
        title = request.form.get('title', '')
        content = request.form.get('content', '')
        if id:
            article = Article.query.filter_by(id=id).first()
            article.title = title
            article.content = content
            db.session.commit()
        else:
            id = RedisClient.get_article_id()
            article = Article(title=title, content=content, id=id)
            db.session.add(article)
            db.session.commit()

        return redirect(url_for('main.article', id=id))


@main.route('/article/comment/<int:article_id>', methods=['POST'])
def comment(article_id):
    name = request.form.get('name', '')
    comment = request.form.get('comment', '')
    id = RedisClient.get_comment_id()
    c = Comment(id=id, name=name, comment=comment, article_id=article_id)
    db.session.add(c)
    db.session.commit()
    return redirect(url_for('main.article', id=article_id))

__author__ = 'zhaojm'

from . import db


# - Article: id,title,content,image,create_at
# - Comment: id,name,comment,create_at,article_id

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    content = db.Column(db.Text)
    image = db.Column(db.String(100))
    create_at = db.Column(db.DateTime)

    def __init__(self, title=None, description=None):
        self.title = title
        self.description = description

        # def __repr__(self):
        #     return '<Activity %r' % (self.title)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    comment = db.Column(db.Text)
    create_at = db.Column(db.DateTime)
    article_id = db.Column(db.Integer)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

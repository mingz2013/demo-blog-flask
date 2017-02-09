__author__ = 'zhaojm'

from sqlalchemy import Column, Integer, String, Text, DateTime

from app.database import Base


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    content = Column(Text)
    image = Column(String(100))
    create_at = Column(DateTime)

    def __init__(self, title=None, description=None):
        self.title = title
        self.description = description

        # def __repr__(self):
        #     return '<Activity %r' % (self.title)


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    comment = Column(Text)
    create_at = Column(DateTime)
    article_id = Column(Integer)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

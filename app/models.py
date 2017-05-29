# -*- coding: utf-8 -*-
from flask import current_app, request
from . import db

class Categories(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    sons = db.relationship('SubCategories',backref='father')
    
    def __repr__(self):
        return '<Categories %r>' % self.name

class SubCategories(db.Model):
    __tablename__='subcategories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    father_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    sons = db.relationship('Articles',backref='father')

    def __repr__(self):
        return '<SubCategories %r>' % self.name

class Articles(db.Model):
    __tablename__='articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, index=True)
    content = db.Column(db.Text)
    date = db.Column(db.String(32))
    father_id = db.Column(db.Integer, db.ForeignKey('subcategories.id'))

    def __repr__(self):
        return '<Articles %r>' % self.title



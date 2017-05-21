from flask import render_template, redirect, url_for, abort, flash, session, request, current_app
from . import main
from ..import db
from ..models import Categories,SubCategories,Articles

@main.route('/', methods=['GET'])
def index():
    CategoriesList = Categories.query.all()
    CategoriesIterator = Categories.query.first()
    SubCategoriesList = SubCategories.query.all()
    SubCategoriesIterator = SubCategories.query.first()
    ArticlesList = Articles.query.all()
    ArticlesIterator = Articles.query.first()
    return render_template('index.html', CategoriesList = CategoriesList, SubCategoriesList = SubCategoriesList, ArticlesList = ArticlesList,\
        CategoriesIterator = CategoriesIterator, SubCategoriesIterator = SubCategoriesIterator, ArticlesIterator = ArticlesIterator,\
        Categories = Categories, SubCategories = SubCategories, Articles = Articles)

@main.route('/ArticleList/<C>/<SC>', methods=['GET'])
def ArticleList(C,SC):
    Category = Categories.query.filter_by(id=C).first()
    if SC != 'No':
        SubCategory = SubCategories.query.filter_by(id=SC).first()
    else:
        SubCategory = None
    CategoriesList = Categories.query.all()
    CategoriesIterator = Categories.query.first()
    SubCategoriesList = SubCategories.query.all()
    SubCategoriesIterator = SubCategories.query.first()
    ArticlesList = Articles.query.all()
    ArticlesIterator = Articles.query.first()
    return render_template('ArticleList.html',Category = Category, SubCategory = SubCategory, \
        CategoriesList = CategoriesList, SubCategoriesList = SubCategoriesList, ArticlesList = ArticlesList,\
        CategoriesIterator = CategoriesIterator, SubCategoriesIterator = SubCategoriesIterator, ArticlesIterator = ArticlesIterator,\
        Categories = Categories, SubCategories = SubCategories, Articles = Articles)

@main.route('/Article/<A>/', methods=['GET'])
def Article(A):
    Article = Articles.query.filter_by(id=A).first()
    CategoriesList = Categories.query.all()
    CategoriesIterator = Categories.query.first()
    SubCategoriesList = SubCategories.query.all()
    SubCategoriesIterator = SubCategories.query.first()
    ArticlesList = Articles.query.all()
    ArticlesIterator = Articles.query.first()
    return render_template('Article.html',Article = Article,\
        CategoriesList = CategoriesList, SubCategoriesList = SubCategoriesList, ArticlesList = ArticlesList,\
        CategoriesIterator = CategoriesIterator, SubCategoriesIterator = SubCategoriesIterator, ArticlesIterator = ArticlesIterator,\
        Categories = Categories, SubCategories = SubCategories, Articles = Articles)

import time
from flask import render_template, redirect, url_for, abort, flash, session, request, current_app
from . import background
from ..import db
from ..models import Categories,SubCategories,Articles
from .forms import CategoryDelForm, CategoryAddForm, CategoryEditForm, SubCategoryDelForm, SubCategoryAddForm, SubCategoryEditForm,\
    ArticleDelForm, ArticleAddForm, ArticleEditForm, TextForm


@background.route('/CategoriesList', methods=['GET', 'POST'])
def CategoriesList():
    if Categories.query.all() == []: 
        empty = True
        Category = None
        CategoriesList = None
        DelForm = None
        EditForm = None
    else: 
        empty = False
        CategoriesList = Categories.query.all()
        Category = CategoriesList[0]
        DelForm = CategoryDelForm()
        DelForm.load_list()
        EditForm = CategoryEditForm()
        EditForm.load_list()
        if DelForm.DelFormSubmit.data and DelForm.validate_on_submit():
            DelFormName = DelForm.CategoriesList.data
            DelCategory = Categories.query.filter_by(id=DelFormName).first()
            if DelCategory.sons:
                for SubCategory in DelCategory.sons:
                    if SubCategory.sons:
                        for Article in SubCategory.sons:
                            db.session.flush()
                            db.session.delete(Article)
                            db.session.commit()
                    db.session.flush()
                    db.session.delete(SubCategory)
                    db.session.commit()
            db.session.flush()
            db.session.delete(DelCategory)
            db.session.commit()
            return redirect(url_for('background.CategoriesList'))
        if EditForm.EditFormSubmit.data and EditForm.validate_on_submit():
            session['BackgroundCategoryId'] = EditForm.CategoriesList.data
            return redirect(url_for('background.Category'))
    AddForm = CategoryAddForm()
    if AddForm.AddFormSubmit.data and AddForm.validate_on_submit():
        NewCategoryName = AddForm.CategoryName.data
        NewCategory = Categories(name = NewCategoryName)
        db.session.flush()
        db.session.add(NewCategory)
        db.session.commit()
        return redirect(url_for('background.CategoriesList'))
    return render_template('background/CategoriesList.html',\
        Category = Category,CategoriesList = CategoriesList,\
        DelForm = DelForm, AddForm = AddForm, EditForm = EditForm,\
        empty = empty)

@background.route('/Category', methods=['GET', 'POST'])
def Category():
    CategoryId = session.get('BackgroundCategoryId')
    Category = Categories.query.filter_by(id=CategoryId).first()
    if Category.sons == []: 
        empty = True
        SubCategory = None
        SubCategoriesList = None
        DelForm = None
        EditForm = None
    else: 
        empty = False
        SubCategoriesList = Category.sons
        SubCategory = SubCategoriesList[0]
        DelForm = SubCategoryDelForm()
        DelForm.load_list(SelectedCategory = Category)
        EditForm = SubCategoryEditForm()
        EditForm.load_list(SelectedCategory = Category)
        if DelForm.DelFormSubmit.data and DelForm.validate_on_submit():
            DelSubCategoryId = DelForm.SubCategoriesList.data
            DelSubCategory = SubCategories.query.filter_by(id=DelSubCategoryId).first()
            if DelSubCategory.sons:
                for Article in DelSubCategory.sons:
                    db.session.flush()
                    db.session.delete(Article)
                    db.session.commit()
            db.session.flush()
            db.session.delete(DelSubCategory)
            db.session.commit()
            return redirect(url_for('background.Category'))
        if EditForm.EditFormSubmit.data and EditForm.validate_on_submit():
            session['BackgroundSubCategoryId'] = EditForm.SubCategoriesList.data
            return redirect(url_for('background.SubCategory'))
    AddForm = SubCategoryAddForm()
    if AddForm.AddFormSubmit.data and AddForm.validate_on_submit():
        NewSubCategoryName = AddForm.SubCategoryName.data
        NewSubCategory = SubCategories(name = NewSubCategoryName, father = Category)
        db.session.flush()
        db.session.add(NewSubCategory)
        db.session.commit()
        return redirect(url_for('background.Category'))
    return render_template('background/Category.html', Category = Category,\
        SubCategory = SubCategory, SubCategoriesList = SubCategoriesList,\
        DelForm = DelForm, AddForm = AddForm, EditForm = EditForm,\
        empty = empty)

@background.route('/SubCategory', methods=['GET', 'POST'])
def SubCategory():
    SubCategoryId = session.get('BackgroundSubCategoryId')
    SubCategory = SubCategories.query.filter_by(id=SubCategoryId).first()
    #flash(SubCategory.name)
    
    if SubCategory.sons == []: 
        empty = True
        Article = None
        ArticlesList = None
        DelForm = None
        EditForm = None
    else: 
        empty = False
        ArticlesList = SubCategory.sons
        Article = ArticlesList[0]
        DelForm = ArticleDelForm()
        DelForm.load_list(SelectedSubCategory = SubCategory)
        EditForm = ArticleEditForm()
        EditForm.load_list(SelectedSubCategory = SubCategory)
        if DelForm.DelFormSubmit.data and DelForm.validate_on_submit():
            DelArticleId = DelForm.ArticlesList.data
            DelArticle = Articles.query.filter_by(id=DelArticleId).first()
            db.session.flush()
            db.session.delete(DelArticle)
            db.session.commit()
            return redirect(url_for('background.SubCategory'))
        if EditForm.EditFormSubmit.data and EditForm.validate_on_submit():
            session['BackgroundArticleId'] = EditForm.ArticlesList.data
            return redirect(url_for('background.EditArticle'))
    AddForm = ArticleAddForm()
    if AddForm.AddFormSubmit.data and AddForm.validate_on_submit():
        session['BackgroundArticleId'] = None
        return redirect(url_for('background.EditArticle'))
    return render_template('background/SubCategory.html', SubCategory = SubCategory,\
        Article = Article, ArticlesList = ArticlesList,\
        DelForm = DelForm, AddForm = AddForm, EditForm = EditForm,\
        empty = empty)
    
    #return render_template('background/Test.html')

@background.route('/EditArticle', methods=['GET', 'POST'])
def EditArticle():
    ArticleId = session.get('BackgroundArticleId')
    SubCategoryId = session.get('BackgroundSubCategoryId')
    SubCategory = SubCategories.query.filter_by(id=SubCategoryId).first()
    form = TextForm()
    Article = None
    if ArticleId != None:     #Load exist Article
        Article = Articles.query.filter_by(id=ArticleId).first()
        if request.method == 'GET':
            form.load_value(OriginalTitle = Article.title, OriginalContent = Article.content)
    if form.validate_on_submit():
        SubmitTitle = form.title.data
        SubmitContent = form.content.data
        SubmitDate = time.strftime("%Y-%m-%d", time.localtime())
        if Article != None:
            db.session.flush()
            db.session.delete(Article)
            db.session.commit()
        Article = Articles(title = SubmitTitle, content = SubmitContent, date = SubmitDate, father = SubCategory)
        db.session.flush()
        db.session.add(Article)
        db.session.commit()
        return redirect(url_for('background.SubCategory'))
    return render_template('background/EditArticle.html', form = form)
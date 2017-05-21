from flask_wtf import FlaskForm
from flaskckeditor import CKEditor
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField, TextAreaField
from wtforms.validators import Required, Length, Email, Regexp
from ..import db
from ..models import Categories, SubCategories, Articles

########################### CATEGORIES

class CategoryDelForm(FlaskForm):
    CategoriesList = SelectField('Caption title:', coerce=int, validators=[Required()])
    DelFormSubmit = SubmitField('Delete Category')

    def load_list(self):
        category = Categories.query.first()
        '''
        for category in Categories.query.all():
             CategoriesNameList.append(category.name)
        self.CategoriesList.choices = CategoriesNameList
        '''
        self.CategoriesList.choices = [(category.id, category.name) for category in Categories.query.all()]

class CategoryAddForm(FlaskForm):
    CategoryName = StringField('Name of new category:', validators = [Required()])
    AddFormSubmit = SubmitField('Add category')

class CategoryEditForm(FlaskForm):
    CategoriesList = SelectField('Caption title:', coerce=int, validators=[Required()])
    EditFormSubmit = SubmitField('Edit Category')

    def load_list(self):
        category = Categories.query.first()
        self.CategoriesList.choices = [(category.id, category.name) for category in Categories.query.all()]

############################# SUBCATEGORIES

class SubCategoryDelForm(FlaskForm):
    SubCategoriesList = SelectField('Subcategory title:', coerce=int, validators=[Required()])
    DelFormSubmit = SubmitField('Delete SubCategory')

    def load_list(self,SelectedCategory):
        subcategory = SubCategories.query.first()
        self.SubCategoriesList.choices = \
        [(subcategory.id, subcategory.name) for subcategory in SubCategories.query.filter_by(father=SelectedCategory).all()]

class SubCategoryAddForm(FlaskForm):
    SubCategoryName = StringField('Name of new subcategory:', validators = [Required()])
    AddFormSubmit = SubmitField('Add subcategory')

class SubCategoryEditForm(FlaskForm):
    SubCategoriesList = SelectField('Subcategory title:', coerce=int, validators=[Required()])
    EditFormSubmit = SubmitField('Edit SubCategory')

    def load_list(self,SelectedCategory):
        subcategory = SubCategories.query.first()
        self.SubCategoriesList.choices = \
        [(subcategory.id, subcategory.name) for subcategory in SubCategories.query.filter_by(father=SelectedCategory).all()]

############################# ARTICLE LIST

class ArticleDelForm(FlaskForm):
    ArticlesList = SelectField('Article title:', coerce=int, validators=[Required()])
    DelFormSubmit = SubmitField('Delete Article')

    def load_list(self,SelectedSubCategory):
        article = Articles.query.first()
        self.ArticlesList.choices = \
        [(article.id, article.title) for article in Articles.query.filter_by(father=SelectedSubCategory).all()]

class ArticleAddForm(FlaskForm):
    AddFormSubmit = SubmitField('Add article')

class ArticleEditForm(FlaskForm):
    ArticlesList = SelectField('Article title:', coerce=int, validators=[Required()])
    EditFormSubmit = SubmitField('Edit Article')

    def load_list(self,SelectedSubCategory):
        article = Articles.query.first()
        self.ArticlesList.choices = \
        [(article.id, article.title) for article in Articles.query.filter_by(father=SelectedSubCategory).all()]

############################# Edit ARTICLE

class TextForm(FlaskForm, CKEditor):
    title = StringField('Title:', validators = [Required()])
    content = TextAreaField()
    submit = SubmitField('Comfirm')
    
    def load_value(self, OriginalTitle, OriginalContent):
        self.title.data = OriginalTitle
        self.content.data = OriginalContent
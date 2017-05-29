#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
from app import create_app, db
from app.models import SubCategories, Categories, Articles
from flask_script import Manager, Shell
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel
from flask import url_for, redirect, session
from flask_admin.contrib.fileadmin import FileAdmin
import os.path as op
from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.widgets import TextArea


class MyView(BaseView):
    @expose('/')
    def index(self):
        return redirect(url_for('main.index'))

class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += " ckeditor"
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()

class PostView(ModelView):
    form_overrides = dict(content=CKTextAreaField)
    can_view_details = True
    create_template = 'admin/post_edit.html'
    edit_template = 'admin/post_edit.html'

class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        arg1 = 'Hello'
        return self.render('admin/welcome.html', arg1=arg1)


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
admin = Admin(
    app,
    index_view=AdminIndexView(
        name='后台首页',
        template='welcome.html',
        url='/admin'
    )
)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
admin.add_view(MyView(name='前台首页'))
admin.add_view(ModelView(Categories, db.session, name = '栏目管理'))
admin.add_view(ModelView(SubCategories, db.session, name = '子栏目管理'))
admin.add_view(PostView(Articles, db.session, name = '文章管理'))
file_path = op.join(op.dirname(__file__), 'app/static')
admin.add_view(FileAdmin(file_path, '/static/', name='资源管理'))




'''
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission,
                Post=Post)
manager.add_command("shell", Shell(make_context=make_shell_context))
'''


if __name__ == '__main__':
    manager.run()

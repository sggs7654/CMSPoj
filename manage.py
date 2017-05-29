#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import create_app, db
from app.models import SubCategories, Categories, Articles
from flask_script import Manager, Shell
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel
from flask import url_for, redirect
'''
class CategoriesView(ModelView):

column_labels = dict(

username=u'用户名',

)
'''

#admin.add_view(UserView(User, db.session, name=u'信息', category=u'用户'))

class MyView(BaseView):
    @expose('/')
    def index(self):
        return redirect(url_for('main.index'))

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
admin = Admin(app)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'

admin.add_view(MyView(name='Index'))
#admin.add_view(

admin.add_view(ModelView(Categories, db.session))
admin.add_view(ModelView(SubCategories, db.session))
admin.add_view(ModelView(Articles, db.session))

'''
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission,
                Post=Post)
manager.add_command("shell", Shell(make_context=make_shell_context))
'''


if __name__ == '__main__':
    manager.run()

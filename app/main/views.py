from flask import render_template, redirect, url_for, abort, flash, session, request, current_app
from . import main
from ..import db

'''
from .forms import RecruitForm
'''
from ..models import Categories,SubCategories,Articles

@main.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html', )


from flask import Blueprint

background = Blueprint('background', __name__)

from . import views

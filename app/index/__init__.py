from flask import Blueprint

bp = Blueprint('index_blueprint', __name__)

from . import views

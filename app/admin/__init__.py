from flask import Blueprint

bp = Blueprint('admin_blueprint', __name__)

from . import views

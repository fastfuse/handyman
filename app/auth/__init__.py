from flask import Blueprint

bp = Blueprint('auth_blueprint', __name__)

from . import views

import os

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from oauthlib.oauth2 import WebApplicationClient

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config.from_object(os.environ['APP_SETTINGS'])

    # User session management setup
    # https://flask-login.readthedocs.io/en/latest
    login_manager = LoginManager()
    login_manager.init_app(app)

    from . import db
    db.init_app(app)

    return app


# OAuth 2 client setup
client = WebApplicationClient(os.environ["GOOGLE_CLIENT_ID"])

from app import views
from app import models

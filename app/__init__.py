import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

load_dotenv()

# Login
login_manager = LoginManager()
login_manager.login_view = 'auth_blueprint.login'

# Database
db = SQLAlchemy()
migrate = Migrate()


# OAuth 2 client setup
# client = WebApplicationClient(os.environ["GOOGLE_CLIENT_ID"])
# client = WebApplicationClient(app.config["GOOGLE_CLIENT_ID"])


def create_app():
    app = Flask(__name__)

    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.index import bp as index_blueprint
    app.register_blueprint(index_blueprint)

    from app.auth import bp as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app


from app import models

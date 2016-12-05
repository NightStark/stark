from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from .nav import nav
from config import basedir


app = Flask(__name__)
app.config.from_object('config')
# Install our Bootstrap extension
Bootstrap(app)


db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)  # lm.setup_app(app)
lm.login_view = 'login'

nav.init_app(app)


# this libs is a file in app dir
from app import views

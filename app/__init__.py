from flask import Flask
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config.from_object('config')
lm = LoginManager()
lm.init_app(app) # lm.setup_app(app)

lm.login_view = 'login'

# this libs is a file in app dir
from app import views

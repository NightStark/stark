from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# this libs is a file in app dir
from app import views

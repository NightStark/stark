CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess-lgg'

import os

# get the dir path of this file(config.py)
basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ = F:\python\flask-app\flask\config.py
# os.path.dirname(__file__) = F:\python\flask-app\flask
# os.path.abspath = 返回规范化的绝对路径。

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

print(basedir)


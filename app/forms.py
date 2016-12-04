from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from .user_op import UserOp


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class SignUpForm(Form, UserOp):
    username = StringField('username', validators=[DataRequired()])
    nickname = StringField('username', validators=[DataRequired()])
    password = StringField('username', validators=[DataRequired()])
    email = StringField('username', validators=[DataRequired()])


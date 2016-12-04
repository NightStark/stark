from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from .user_op import UserOp


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('username', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    checker = UserOp()

    def login_check(self):
        self.checker.user_op_login_check(self)

    def username_is_invalid(self):
        return self.checker.username_is_invalid

    def password_is_invalid(self):
        return self.checker.password_is_invalid


class SignUpForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('username', validators=[DataRequired()])
    nickname = StringField('username', validators=[DataRequired()])
    email = StringField('username', validators=[DataRequired()])
    checker = UserOp()

    def user_op_check(self):
        # checker = UserOp(self.username.data, self.password.data, self.nickname.data, self.email.data)
        self.checker.user_op_check(self)

    def user_op_get_error(self):
        return self.checker.username_is_exit or self.checker.nickname_is_exit or self.checker.email_is_exit

    def user_op_login_check(self):
        self.checker.user_op_login_check(self)




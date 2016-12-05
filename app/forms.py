from flask_wtf import Form
from wtforms import StringField, BooleanField, SubmitField
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

    def user_op_get_user(self):
        return self.checker.user


class SignUpForm(Form):
    username = StringField('username', validators=[DataRequired()], description='your username')
    password = StringField('password', validators=[DataRequired()], description='your password')
    nickname = StringField('nickname', validators=[DataRequired()], description='your nickname')
    email = StringField('email', validators=[DataRequired()], description='your email')
    submit_button = SubmitField('Submit Form')

    checker = UserOp()

    def user_op_check(self):
        # checker = UserOp(self.username.data, self.password.data, self.nickname.data, self.email.data)
        self.checker.user_op_check(self)

    def user_op_get_error(self):
        return self.checker.username_is_exit or self.checker.nickname_is_exit or self.checker.email_is_exit

    def user_op_login_check(self):
        self.checker.user_op_login_check(self)


class RemoteCmdForm(Form):
    remote_cmd_name = StringField('remote_cmd_name', validators=[DataRequired()])
    remote_cmd = StringField('remote_cmd', validators=[DataRequired()])






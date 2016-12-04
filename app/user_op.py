from app import db, models


class UserOp:

    def __init__(self):
        self.username_is_exit = False
        self.nickname_is_exit = False
        self.email_is_exit = False
        self.get_error = False
        self.create_user_success =False

    def user_op_check(self, form):
        self.get_error = False
        self.username_is_exit = False
        self.nickname_is_exit = False
        self.email_is_exit = False
        print("username_is_exit")
        old_user = models.User.query.filter_by(username=form.username.data).first()
        if old_user is not None:
            self.username_is_exit = True
            self.get_error = True
            print("username_is_exit")

        old_user = models.User.query.filter_by(nickname=form.nickname.data).first()
        if old_user is not None:
            self.nickname_is_exit = False
            self.get_error = True
            print("nickname_is_exit")

        old_user = models.User.query.filter_by(email=form.email.data).first()
        if old_user is not None:
            self.email_is_exit = True
            self.get_error = True
            print("email_is_exit")

    def user_op_create(self, form):
        user = models.User(username=form.username.data, password=form.password.data, nickname=form.email.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        self.create_user_success = True


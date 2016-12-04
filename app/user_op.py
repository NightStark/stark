from app import db, models


class UserOp:

    username_is_exit = False
    nickname_is_exit = False
    email_is_exit = False

    def __init__(self, username, nickname, email, password):
        self.username = username
        self.nickname = nickname
        self.email = email
        self.password = password

    def user_op_check(self):

        old_user = models.User.query.filter_by(username=self.username).first()
        if old_user is not None:
            self.username_is_exit = True
        old_user = models.User.query.filter_by(self.email).first()
        if old_user is not None:
            self.username_is_exit = True
        old_user = models.User.query.filter_by(email=self.email).first()
        if old_user is not None:
            self.username_is_exit = True

    def user_op_create(self):
        user = models.User(username=self.username, password=self.password, nickname=self.email, email=self.email)
        db.session.add(user)
        db.session.commit()


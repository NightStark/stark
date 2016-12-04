from app import db

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), index=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    access = db.relationship('Access', backref='author', lazy="dynamic")

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return True

    # @staticmethod with this can not be call , at others place
    def get_id(self):  # login_user, will call this func
        # return unicode(self.id)
        print("get_id get id")
        print(self.id.__str__())
        return self.id.__str__()

    def get(self):
        return self

    def __repr__(self):
        return '<User:%r>' % self.nickname


class Access(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    administrator = db.Column(db.Boolean)
    connect_server = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % self.body



ROLE_USER = 0
ROLE_ADMIN = 1


class User:
    id = 1
    name = "lgg"

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return True

    @staticmethod
    def get_id():
        # return unicode(self.id)
        print("get id")
        return id.__str__()

    def get(self):
        return self


from app import db, models

user = models.User(username="aa", password="123", email="lyj@16.com")
db.session.add(user)
db.session.commit()

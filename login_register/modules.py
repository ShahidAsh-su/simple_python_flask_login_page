from login_register import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))

class User(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   emailid = db.Column(db.String(120),nullable=False,unique=True)
   username = db.Column(db.String(120),nullable=False,unique=True)
   password = db.Column(db.String(120),nullable=False)
   phone = db.Column(db.Integer)


   def __repr__(self):
        return '<User %r>' % self.username

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   emailId = db.Column(db.String(120),nullable=False,unique=True)
   password = db.Column(db.String(120),nullable=False, unique=True)
   e = db.Column(db.String(123))

   def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/register')
def register():
   return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
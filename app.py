from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   emailid = db.Column(db.String(120),nullable=False,unique=True)
   username = db.Column(db.String(120),nullable=False,unique=True)
   password = db.Column(db.String(120),nullable=False, unique=True)
   phone = db.Column(db.Integer,nullable=False)


   def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def home():
   users = User.query.all()
   return render_template('home.html', users = users)

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/register')
def register():
   return render_template('register.html')

@app.route("/register_data", methods=['POST'])
def register_data():
   #if request.methods == 'POST':
   username = request.form['username']
   emailid = request.form['email']
   password = request.form['password']
   phone = request.form['phone']
   new_user = User(username=username, password=password,emailid=emailid,phone=phone)
   try:
      db.session.add(new_user)
      db.session.commit()
      return redirect("/")
   except:
      msg = 'Username or Email already exists'
      return render_template('register.html',msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, url_for, request, redirect, flash
from login_register.forms import RegistrationForm ,  LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a433dad2ba8dbbb9ac25798b94fedab0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   emailid = db.Column(db.String(120),nullable=False,unique=True)
   username = db.Column(db.String(120),nullable=False,unique=True)
   password = db.Column(db.String(120),nullable=False)
   phone = db.Column(db.Integer,nullable=False)


   def __repr__(self):
        return '<User %r>' % self.username




@app.route('/')
def home():
   # users = User.query.all()
   return render_template('home.html')




@app.route('/login', methods=['POST', 'GET'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
      if form.email.data == 'afridis911@gmail.com' and form.password.data == '111111':
         flash(f'Log in successfull {form.email.data}','success')
         return redirect(url_for('home'))
      else:
         flash('Unsuccessfull','danger')
   return render_template('login.html', form = form)




@app.route('/register', methods=['GET','POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
      flash(f'Account created for {form.username.data}','success')
      return redirect(url_for('login'))
   return render_template('register.html', form=form)

from flask import render_template, url_for, request, redirect, flash
from login_register.forms import RegistrationForm ,  LoginForm
from login_register.modules import User
from login_register import app, bcrypt, db
from flask_login import login_user



@app.route('/')
def home():
   # users = User.query.all()
   return render_template('home.html')




@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       user = User.query.filter_by(emailid=form.email.data).first()
       if user and bcrypt.check_password_hash(user.password, form.password.data):
           login_user(user, remember=form.remember.data)
           return redirect(url_for('home'))
       else:
           flash('Unsuccessfull, Please check your email and password','danger')
    return render_template('login.html', form = form)




@app.route('/register', methods=['GET','POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
      username = form.username.data
      email = form.email.data
      password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=username, emailid=email, password=password)
      try:
         db.session.add(user)
         db.session.commit()
         flash(f'Account created for {form.username.data}','success')
         return redirect(url_for('login'))
      except:
         flash('Failed','danger')
   return render_template('register.html', form=form)

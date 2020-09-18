from flask import render_template, url_for, request, redirect, flash
from login_register.forms import RegistrationForm ,  LoginForm
from login_register.modules import User
from login_register import app, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/')
def home():
   # users = User.query.all()
   return render_template('home.html')


@app.route('/logged_in')
@login_required
def logged():
    # user = User
    return render_template('success.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
       emailid = User.query.filter_by(emailid=form.email.data).first()
       user =  User.query.filter_by(username=form.email.data).first()
       flag = False
       try:
           flag = bcrypt.check_password_hash(user.password, form.password.data)
       except:
           pass
       try:
           flag = bcrypt.check_password_hash(emailid.password, form.password.data)
       except:
           pass 
       if ((user or emailid) and flag) :
           login_user(user or emailid, remember=form.remember.data)
           next_page = request.args.get('next')
           return redirect(next_page) if next_page else redirect(url_for('home'))
       else:
           flash('Incorrect, Please check your Email/Username and Password','danger')
    return render_template('login.html', form = form)




@app.route('/register', methods=['GET','POST'])
def register():
   if current_user.is_authenticated:
      return redirect(url_for('home'))
   form = RegistrationForm()
   if form.validate_on_submit():
      name = form.name.data
      username = form.username.data
      email = form.email.data
      blood_group = form.blood_group.data
      password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=username, emailid=email, password=password, blood_group=blood_group, name=name)
      try:
         db.session.add(user)
         db.session.commit()
         flash(f'Account created for {form.username.data}','success')
         return redirect(url_for('login'))
      except:
         flash('Failed','danger')
   return render_template('register.html', form=form)


@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('home'))

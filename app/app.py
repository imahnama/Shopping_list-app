import os
from flask import Flask, url_for,render_template, request, flash, redirect, session
#import the user object
from app import User_obj

#create the flask app
app = Flask(__name__, template_folder='../templates', static_folder='../assets')
app.config.from_object(__name__)
app.config.update(dict(
    SECRET_KEY='topsecretkey',
    #this should be set to false in production
    DEBUG=True
))
@app.route('/  <div class="row container">
    <div class="col-md-6 col-md-offset-7 back">
      <h1 class="text-center">Sign Up</h1>
      {% with messages = get_flashed_messages(with_categories=true) %}
  		{% if messages %}
  		{% for category, message in messages %}
      <div class="alert {{category}} fade in">
          <a href="#" class="close" data-dismiss="alert">&times;</a>
          <strong>{{message}}</strong>
      </div>
   	 	{% endfor %}
   	 	{% endif %}
   	 	{% endwith %}
    <form action="{{url_for("register")}}" method="POST" name="signup">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="name" class="form-control" name="username" placeholder="Username">
      </div>
  <div class="form-group">
    <label for="Email">Email address</label>
    <input type="email" class="form-control" name="email" aria-describedby="emailHelp" placeholder="Enter email">
  </div>
  <div class="form-group">
    <label for="Password">Password</label>
    <input type="password" class="form-control" name="password" minlength="6" placeholder="Password">
  </div>
  <div class="form-group">
    <label for="confpassword">Confirm Password</label>
    <input type="password" class="form-control" name="confpassword" placeholder="Confirm Password">
  </div>
  <button type="submit" class="center btn btn-primary">Sign up</button>
</form>
  </div>
</div>')
def index():
    """route to render home page"""
    return render_template('index.html')

@app.route('/login')
def login():
    """route to render login page"""
    return render_template('login.html')

@app.route('/signup')
def signup():
    """route to render signup page and register new user"""
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard_view():
    """route to render dashboard page"""
    return render_template('dashboard.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    # counter check if password is the same
    password = request.form['password']
    confpassword = request.form['confpassword']

    if password != confpassword:
        flash('passwords do not match', 'alert-danger')
        return redirect(url_for('signup'))
    res = User_obj.signup(username, email, password)
    if res == "username or email exists":
        flash('username or email already taken', 'alert-danger')
        return redirect(url_for('signup'))
    flash('signup successful. now login', 'alert-success')
    return redirect(url_for('login'))

@app.route ('/session', methods =['POST'])
def session ():
    username = request.form['username']
    password = request.form['password']
    res = User_obj.login(username=username, password=password)
    print(res)
    if res == True:
        return redirect(url_for('dashboard_view'))
    else:
        flash('wrong username or password', 'alert-danger')
        return redirect(url_for('login'))
@app.route ('/newlist')
def newlist():
    if is_logged_in():
        return render_template('newlist.html')
    else:
        return redirect(url_for('loginview'))
    return render_template('newlist.html')

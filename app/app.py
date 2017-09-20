import os
from flask import Flask, url_for,render_template

#create the flask app
app = Flask(__name__, template_folder='Designs', static_folder='../assets')
app.config.from_object(__name__)
app.config.update(dict(
    SECRET_KEY='topsecretkey',
    USERNAME='admin',
    PASSWORD='default',
    #this should be set to false in production
    DEBUG = True
))
@app.route('/')
def index():
    """route to render home page"""
    return render_template('index.html')

@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/signup')
def signup_view():
    return render_template('signup.html')

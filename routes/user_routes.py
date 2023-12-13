from routes import app
from flask import render_template

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/login')
def login_page():
    return render_template('login.html')
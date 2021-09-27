from app import my_app
from flask import render_template

@my_app.route('/')
@my_app.route('/index')
def index():
    return render_template("main.html")
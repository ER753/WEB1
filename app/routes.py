from flask import render_template
from app import app

@app.route('/')
def hello():
    return"Hello World!!"
@app.route('/index')
def index():
    return render_template('index.html',title='Home')
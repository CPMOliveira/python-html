from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Cristiano'}
    posts = [
        {'author': {'username': 'Maria'}, 'body': 'Hello from Maria!'},
        {'author': {'username': 'Mário'}, 'body': 'Hello!'}
    ]
    return render_template('index.html', user=user, posts=posts)
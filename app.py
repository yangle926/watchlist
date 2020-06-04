from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>欢迎！</h1><img src="img/mm01.jpg">'


@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='greyli'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'

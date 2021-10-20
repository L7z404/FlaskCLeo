from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import flash
from flask import g
from flask.helpers import url_for
from flask import redirect
from flask_wtf import CSRFProtect
from wtforms import form
from config import DevelopmentConfig

from models import db 
from models import User

import forms
import json

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e): 
    return render_template('404.html'), 404

@app.before_request
def before_request(): 
    pass

@app.after_request
def after_request(response): 
    return response

@app.route('/')
def index(): 
    # custom_cookie = request.cookies.get('custom_cookie', 'Undefined')
    # print(custom_cookie)
    if 'username' in session: 
        username = session['username']
        print(username)
    title = 'Index'
    return render_template('index.html', title=title)

@app.route('/logout')
def logout(): 
    if 'username' in session: 
        session.pop('username') 
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login(): 
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate(): 
        username = login_form.username.data
        success_message = 'Bienvenido {}'.format(username)
        flash(success_message)
        session['username'] = login_form.username.data
        
    title = 'Login'
    return render_template('login.html', title=title, form = login_form)

@app.route('/comment', methods = ['GET', 'POST'])
def comment():
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate(): 
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else: 
        print("Error en el formulario")
    
    title = 'Curso Flask'
    return render_template('comment.html', title = title, form = comment_form)

@app.route('/create', methods = ['GET', 'POST'])
def create(): 
    create_form = forms.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate(): 
        user = User(create_form.username.data,
                    create_form.password.data,
                    create_form.email.data)
        db.session.add(user)
        db.session.commit()
        success_message = 'Usuario registrado en la base de datos'
        flash(success_message)
    return render_template('create.html', form=create_form)

@app.route('/cookie')
def cookie(): 
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custom_cookie', 'La cookie de Leonel')
    return response

@app.route('/ajax-login', methods = ['POST'])
def ajax_login(): 
    print(request.form)
    username = request.form['username']
    response = {'status':200, 'username':username, 'id':1}
    return json.dumps(response)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    app.run(port=8000)
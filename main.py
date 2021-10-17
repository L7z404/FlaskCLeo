from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask_wtf import CsrfProtect

import forms

app = Flask(__name__)
app.secret_key = 'secret'
csrf = CsrfProtect(app)

@app.route('/')
def index(): 
    custom_cookie = request.cookies.get('custom_cookie', 'Undefined')
    print(custom_cookie)
    title = 'Index'
    return render_template('index.html', title=title)

@app.route('/login', methods = ['GET', 'POST'])
def login(): 
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate(): 
        print(login_form.username.data)
        print(login_form.password.data)
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
    return render_template('index.html', title = title, form = comment_form)

@app.route('/cookie')
def cookie(): 
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custom_cookie', 'La cookie de Leonel')
    return response

if __name__ == '__main__':
    app.run(debug=True, port=8000)
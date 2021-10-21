from wtforms import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField
from wtforms import validators

from models import User

def length_honeypot(form, field): 
    if len(field.data) > 0: 
        raise validators.ValidationError('El campo debe estar vacío.')

class CommentForm(Form):
    comment = TextField('Comentario')
    honeypot = HiddenField('', [length_honeypot])

class LoginForm(Form): 
    username = StringField('Nombre de Usuario', [
        validators.Required(message= 'El nombre de usuario es requerido'),
        validators.length(min=4, max=25, message='Ingrese un nombre de usuario válido')
    ])
    password = PasswordField('Contraseña', [
        validators.Required(message='La contraseña es requerida')
    ])

class CreateForm(Form): 
    username = TextField('Nombre de Usuario', [
        validators.Required(message= 'El nombre de usuario es requerido'),
        validators.length(min=4, max=50, message='Ingrese un nombre de usuario válido')
    ])
    email = EmailField('Correo Electronico', [
        validators.Required(message='El email es requerido'),
        validators.Email(message='Ingrese un email válido'),
        validators.length(min=4, max=50, message="Ingrese un email válido")
    ])
    password = PasswordField('Contraseña', [
        validators.Required(message='La contraseña es requerida')
    ])
    
    def validate_username(form, field): 
        username = field.data
        user = User.query.filter_by(username=username).first()
        if user is not None: 
            raise validators.ValidationError('El nombre de usuario ya se encuentra registrado')
import os
import pymysql

from flask_sqlalchemy import SQLAlchemy
class Config(object): 
    SECRET_KEY = 'secret'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'leonel.castillo@alumnos.udg.mx'
    MAIL_PASSWORD = 'FD78c8F45D'

class DevelopmentConfig(Config): 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
import os
import pymysql

from flask_sqlalchemy import SQLAlchemy
class Config(object): 
    SECRET_KEY = 'secret'

class DevelopmentConfig(Config): 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
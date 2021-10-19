import os

from flask_sqlalchemy import SQLAlchemy
class Config(object): 
    SECRET_KEY = 'secret'

class DevelopmentConfig(Config): 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask'
    
    #Vas en el minuto 7:55 del video 24
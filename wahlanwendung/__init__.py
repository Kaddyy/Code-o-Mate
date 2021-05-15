from flask import Flask
from flask_admin import Admin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from os import environ, path

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daten.db'
# track database changes
SQLALCHEMY_TRACK_MODIFICATION = True
SECRET_KEY = 'mydarksecret'
# choose admin-theme
FLASK_ADMIN_SWATCH = 'cerulean'

db = SQLAlchemy(app)
migrate= Migrate(app, db)

from wahlanwendung import models

admin = Admin(app, name='Code-o-Mate', template_mode='bootstrap3')
from wahlanwendung import admin_models

from wahlanwendung import main



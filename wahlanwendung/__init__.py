from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

db = SQLAlchemy(app)

from wahlanwendung import models
from wahlanwendung import wahlanwendung



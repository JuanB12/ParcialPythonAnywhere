import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "mysql+pymysql://root@localhost/parcialMovil")
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

app.secret_key = os.environ.get("SECRET_KEY", "cambia-esta-clave")

db = SQLAlchemy(app)

ma = Marshmallow(app)
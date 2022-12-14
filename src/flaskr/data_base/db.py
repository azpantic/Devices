from flaskr.app import app
from flask_sqlalchemy import SQLAlchemy

db : SQLAlchemy = SQLAlchemy(app)
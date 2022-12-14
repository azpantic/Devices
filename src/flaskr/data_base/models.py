from .db import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer , Enum , DateTime
import enum

class UserTypes(enum.Enum):

    administrator = 1
    regular_user = 2
    
class Device(db.Model):
    
    id = db.Column(db.Integer , primary_key = True)
    uid = db.Column(db.Integer , nullable = False)
    title = db.Column(db.String(50) ,nullable = False)
    description = db.Column(db.String(200) ,nullable = True)

class User(db.Model):
    
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(50) ,nullable = False)
    email = db.Column(db.String(50) ,nullable = False)
    password = db.Column(db.String(50) ,nullable = False)
    type = db.Column(Enum(UserTypes), nullable = False)

class Operation(db.Model):
    
    id = db.Column(db.Integer , primary_key = True)
    userId = db.Column(db.Integer , primary_key = False)
    deviceId = db.Column(db.Integer , primary_key = False)
    startTime = db.Column(db.DateTime , nullable = False)
    endTime = db.Column(db.DateTime , nullable = False)

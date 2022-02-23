from . import db
from flask_login import UserMixin
from sqlalchemy import func

class Detects(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    sensor=db.Column(db.String(150))
    pet=db.Column(db.String(150))
    captured=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id= db.Column(db.Integer,primary_key=True)
    email= db.Column(db.Strinh(150),unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    captures=db.relationship('Detects')
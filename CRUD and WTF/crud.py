import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir=os.path.abspath(os.path.dirname(__file__))
#_file--> C://users/adithya/doc/crud.property
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

######
class Puppy(db.Model):
    __tablename__="puppies"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Integer)

    def __init__(self,name,age):
        self.name=name
        self.name=age
    def __repr__(self):
        return f"puppy {self.name}is {self.age} years old"

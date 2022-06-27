from flask import Flask, render_template, flash, redirect
import time
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///Users.db'
app.config['SECRET_KEY'] = 'Frosty mangoes'

db = SQLAlchemy(app)

t = SubmitField('Submit')

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(128))
    
    def __init__(self, name, password):
        self.name = name
        self.password = password
        

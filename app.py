from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///Users.db'

@app.route('/test')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

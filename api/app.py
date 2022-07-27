import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from route.home import home_api

app=Flask(__name__)

#  routing
@app.route('/')
def home():
   return "<h1>hello world!</h1>"

app.register_blueprint(home_api)

#  database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

db.create_all()
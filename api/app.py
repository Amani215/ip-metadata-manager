from flask import Flask

app=Flask(__name__)

# Create tables
from model import db
from model.user import User

# db.drop_all()
db.create_all()

#  routing
from route.user import user_api
from route.auth import auth_api

app.register_blueprint(user_api)
app.register_blueprint(auth_api)

@app.route('/')
def home():
   return "<h1>hello world!</h1>"
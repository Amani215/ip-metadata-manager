from flask import Flask
from route.home import home_api

app=Flask(__name__)

# Create tables
from model import db
from model.user import User

db.create_all()

# Add sample user

# guest = User(name='guest')
# db.session.add(guest)
# db.session.commit()

#  routing
from route.crud import crud

app.register_blueprint(crud)
app.register_blueprint(home_api)

@app.route('/')
def home():
   return "<h1>hello world!</h1>"
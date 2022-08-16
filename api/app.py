from flask import Flask
from flask_openapi3 import OpenAPI, Info

info = Info(title='IP metadata API', version='1.0.0')
app=OpenAPI(__name__, info = info)

import config

# Create tables
from model import db
from model.user import User

# db.drop_all()
db.create_all()

#  routing
from route.user import user_api
from route.auth import auth_api

# app.register_blueprint(user_api)
# app.register_blueprint(auth_api)
app.register_api(user_api)

@app.route('/')
def home():
   return "<h1>hello world!</h1>"

if __name__ == '__main__':
    app.run()
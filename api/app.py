from flask import Flask
from route.home import home_api

app=Flask(__name__)

@app.route('/')
def home():
   return "<h1>hello world!</h1>"

app.register_blueprint(home_api)
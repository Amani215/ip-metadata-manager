from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from route.home import home_api

app=Flask(__name__)

#  routing
@app.route('/')
def home():
   return "<h1>hello world!</h1>"

app.register_blueprint(home_api)

#  database
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
# db = SQLAlchemy(app)

from model import Base, engine
from model.user import User

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)

ed_user = User(name='ed')
session.add(ed_user)

# our_user = session.query(User).filter_by(name='ed').first()
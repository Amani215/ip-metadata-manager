import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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

from sqlalchemy.orm import sessionmaker

_DB_URI = 'postgresql://db:pass@db:5432/db'
engine = create_engine(_DB_URI)

Base = declarative_base()

# from api.model.user import User

Base.metadata.create_all(engine)

# session = sessionmaker(bind=engine)

# ed_user = User(name='ed')
# session.add(ed_user)

# our_user = session.query(User).filter_by(name='ed').first()
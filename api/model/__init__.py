from flask_sqlalchemy import SQLAlchemy
from app import app

# Setup db

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://db:pass@db:5432/db'
db = SQLAlchemy(app)
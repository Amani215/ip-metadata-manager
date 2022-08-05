from flask_sqlalchemy import SQLAlchemy
from app import app

# Setup db
app.config['SECRET_KEY']='903900a2865fbcc43f5752851729f6ef'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://db:pass@db:5432/db'
db = SQLAlchemy(app)
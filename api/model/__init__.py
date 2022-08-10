from flask_sqlalchemy import SQLAlchemy
from app import app

# Setup db
db = SQLAlchemy(app)
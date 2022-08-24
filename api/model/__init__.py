from flask_sqlalchemy import SQLAlchemy
from app import app

# Setup db
db = SQLAlchemy(app)

# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('postgresql://db:pass@db:5432/db', convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
# Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_DB_URI = 'sqlite:///:memory:'
engine = create_engine(_DB_URI)

Base = declarative_base()
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

from .user import User
from .budget import Budget
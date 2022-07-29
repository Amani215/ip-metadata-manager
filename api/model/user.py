from sqlalchemy import Column, Integer, String
from api.model import Base
from app import db

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String(80), unique=True, nullable=False)

  def __init__(self, name):
    self.name = name
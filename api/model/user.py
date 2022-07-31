from sqlalchemy import Column, Integer, String
from app import db

class User(db.Model):
  id = Column(Integer, primary_key=True)
  name = Column(String(80), unique=True, nullable=False)

  def __init__(self, name):
    self.name = name

  @property
  def serialize(self):
      """Return object data in easily serializable format"""
      return {
          'id'         : self.id,
          'name': self.name
      }
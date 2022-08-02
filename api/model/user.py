from sqlalchemy import Column, Integer, String, true
from app import db

class User(db.Model):
  id = Column(Integer, primary_key=True)
  username = Column(String(80), unique=True, nullable=False)
  password = Column(String(128), nullable=False)

  def __init__(self, username, password):
    self.username = username
    self.password  = password

  @property
  def serialize(self):
      """Return object data in easily serializable format"""
      return {
          'id'  : self.id,
          'username': self.username,
          'password': self.password
      }
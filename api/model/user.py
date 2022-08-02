from sqlalchemy import Column, Integer, String
from app import db
from bcrypt import hashpw, checkpw, gensalt

class User(db.Model):
  id = Column(Integer, primary_key=True)
  name = Column(String(80), nullable=False)
  password = Column(String(128), nullable=False)

  def __init__(self, name, password):
    self.name = name
    self.password  = hashpw(password.encode('utf-8'), gensalt())

  # def set_password(self, password):
  #     self.password_hash = generate_password_hash(password)

  # def check_password(self, password):
  #     return check_password_hash(self.password_hash, password)

  @property
  def serialize(self):
      """Return object data in easily serializable format"""
      return {
          'id'  : self.id,
          'name': self.name,
          'password': self.password
      }
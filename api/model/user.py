from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
from app import db
import uuid

class User(db.Model):
  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
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
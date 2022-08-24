from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
from .user import User
from app import db
from service import user as user_service
import uuid

class IPAddress(db.Model):
  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  address = Column(String(80), nullable=False)
  userID = Column(UUID(as_uuid=True), nullable=False)

  def __init__(self, address, username):
    self.address = address
    self.userID  = user_service.get_by_username(username).id

  @property
  def serialize(self):
      """Return object data in easily serializable format"""
      return {
          'id'  : self.id,
          'address': self.address,
          'username': self.userID
      }
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, CHAR, JSON, TIMESTAMP, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import BIT, INTEGER, TINYINT

from .database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True, nullable=False)
    email = Column(String(32), unique=True, index=True)
    usr_username = Column(String(45))
    hashed_password = Column(String(32))
    usr_name = Column(String(45))
    usr_lastname = Column(String(45))
    usr_created = Column(TIMESTAMP)
    usr_updated = Column(TIMESTAMP)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")


    
class Item(Base):

    __tablename__ = "items"


    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(32), index=True)
    description = Column(String(32), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
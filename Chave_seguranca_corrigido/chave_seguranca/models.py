from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)

    credentials = relationship("Credential", back_populates="owner")


class Credential(Base):
    __tablename__ = "credentials"

    id = Column(Integer, primary_key=True)
    site = Column(String)
    username = Column(String)
    password_encrypted = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="credentials")

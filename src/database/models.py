from sqlalchemy import Column, Integer, String
from .base import Base


class Person(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    login = Column(String)
    password = Column(String)

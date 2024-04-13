#!/usr/bin/python3
"""Module that defines a class State"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class State(Base):
    """inherits from base and is linked to table state"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    """Establish a one-to-many relationship with City"""
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

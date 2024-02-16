#!/usr/bin/python3
"""
This module defines a State class that inherits from Base.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    This class is linked to the states table and has a relationship
    with the City class.

    Attributes:
        id (Column): The state's id.
        name (Column): The state's name.
        cities (relationship): The cities in the state.
    """

    __tablename__ = "states"
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement="auto"
            )
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City",
            back_populates="state",
            cascade="all, delete"
            )

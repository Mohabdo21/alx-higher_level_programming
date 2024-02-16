#!/usr/bin/python3
"""
This module defines a City class that inherits from Base.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from relationship_state import Base, State


class City(Base):
    """
    This class is linked to the cities table and has a relationship
    with the State class.

    Attributes:
        id (Column): The city's id.
        name (Column): The city's name.
        state_id (Column): The id of the state the city is in.
        state (relationship): The state the city is in.
    """

    __tablename__ = "cities"
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement="auto"
            )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")

#!/usr/bin/python3
"""Module to define a City class"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from model_state import Base, State


class City(Base):
    """City class"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

#!/usr/bin/python3
"""
This module defines a State class that inherits from Base.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    This class is linked to the states table.

    Attributes:
        id (Column): The state's id.
        name (Column): The state's name.
    """

    __tablename__ = "states"
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement="auto"
            )
    name = Column(String(128), nullable=False)

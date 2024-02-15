#!/usr/bin/python3
"""
Module to delete all State objects from a
database where name contains 'a'
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username,
            password,
            database
            ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like("%a%")):
        session.delete(state)

    session.commit()
    session.close()

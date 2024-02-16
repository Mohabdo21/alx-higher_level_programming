#!/usr/bin/python3
"""Module to list all City objects from a database"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_city import City
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

    for city, state in (
        session.query(City, State).filter(
            City.state_id == State.id
            ).order_by(City.id)
    ):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

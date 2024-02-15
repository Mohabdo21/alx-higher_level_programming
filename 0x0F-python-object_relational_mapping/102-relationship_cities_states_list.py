#!/usr/bin/python3
"""
Module to list all City objects from a database
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_city import City
from relationship_state import Base, State

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

    for city in session.query(City).join(State).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()

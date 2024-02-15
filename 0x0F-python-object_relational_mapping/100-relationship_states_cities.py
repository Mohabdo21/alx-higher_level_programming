#!/usr/bin/python3
"""
This module contains a script that adds a new 'State' object 'California'
and a new 'City' object 'San Francisco' to a specified database.
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))

    session.commit()

    session.close()

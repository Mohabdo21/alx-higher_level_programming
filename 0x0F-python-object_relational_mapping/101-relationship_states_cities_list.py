#!/usr/bin/python3
"""
Module to list all State objects and corresponding City objects from a database
"""
if __name__ == "__main__":

    import sys

    from sqlalchemy import create_engine
    from sqlalchemy.orm import joinedload, sessionmaker

    from relationship_city import City
    from relationship_state import State

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

    for state in (
        session.query(State).options(
            joinedload(State.cities)
            ).order_by(State.id)
    ):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()

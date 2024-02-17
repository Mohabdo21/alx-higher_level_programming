#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects from a database.

Usage: script.py <username> <password> <database>

- username: MySQL username
- password: MySQL password
- database: Database name
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload, sessionmaker

from relationship_city import City
from relationship_state import State


def main():
    """Connects to a database, retrieves data, and prints results."""

    # Check command-line arguments
    if len(sys.argv) != 4:
        print("Usage: script.py <username> <password> <database>")
        sys.exit(1)

    # Retrieve credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Create SQLAlchemy engine with appropriate connection string
        engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
            pool_pre_ping=True,
        )

        # Create session using sessionmaker
        Session = sessionmaker(bind=engine)
        session = Session()

        for state in session.query(State):
            print('{}: {}'.format(state.id, state.name))
        # Query states with eager loading for cities, ordered by state ID
#        for state in (
#            session.query(State)
#            .options(joinedload(State.cities))
#            .outerjoin(City)
#            .order_by(State.id, City.id)
#        ):
#            print(f"{state.id}: {state.name}")
#            for city in state.cities:
#                print(f"\t{city.id}: {city.name}")

    except SQLAlchemyError as e:
        print(f"Database error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        session.close()


if __name__ == "__main__":
    main()

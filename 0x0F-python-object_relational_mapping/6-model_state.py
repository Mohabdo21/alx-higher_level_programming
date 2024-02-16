#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys

from sqlalchemy import create_engine

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

    Base.metadata.create_all(engine)

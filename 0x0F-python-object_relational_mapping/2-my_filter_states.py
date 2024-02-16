#!/usr/bin/python3
"""Module to list all states from a database where name matches the argument"""

import sys

import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
            state_name
            )
    )
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

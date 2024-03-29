#!/usr/bin/python3
"""Module to list all states from a database starting with N"""

import sys

import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
            )
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

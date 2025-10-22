#!/usr/bin/python3
"""this is a python command to list all states in asc order by id"""

import MySQLdb
import sys


def list_all_states():
    """connect to mysql and lists all states in asc order by id."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connect to mysql server
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()

    # use cursor to do mysql order - select all states ordered by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N' ORDER BY id ASC")

    # fetch and print
    all_states = cursor.fetchall()
    for state in all_states:
        print(state)

    # remove cursor and connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    list_all_states()

#!/usr/bin/python3
"""this is a python command to filter states"""


import MySQLdb
import sys


def list_all_states():
    """connect to mysql and filter states."""
    """SELECT * FROM states WHERE name = 'Arizona' ORDER BY id ASC"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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
    cursor.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
        .format(state_name)
        )

    # fetch and print
    all_states = cursor.fetchall()
    for state in all_states:
        print(state)

    # remove cursor and connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    list_all_states()

#!/usr/bin/python3
"""this is a python command to filter states"""


import MySQLdb
import sys


def safe_filter_states():
    """connect to MySQL and print states whose name matches the argument"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    connect = None
    cursor = None
    try:
        connect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = connect.cursor()

        # query has parameters to prevent injection
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        # log error
        sys.stderr.write("Database error: {}\n".format(e))
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()

if __name__ == "__main__":
    safe_filter_states()


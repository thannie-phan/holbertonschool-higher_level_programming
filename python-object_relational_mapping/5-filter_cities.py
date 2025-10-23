#!/usr/bin/python3
"""this is a python command to list all cities from database"""


import MySQLdb
import sys


def list_filter_cities():
    """connect to MySQL and list all cities from database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    states_name = sys.argv[4]

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
        query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
        cursor.execute(query, (states_name,))

        rows = cursor.fetchall()
        city_names = [row[1] for row in rows]
        print(", ".join(city_names))

    except MySQLdb.Error as e:
        # log error
        sys.stderr.write("Database error: {}\n".format(e))
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()


if __name__ == "__main__":
    list_filter_cities()

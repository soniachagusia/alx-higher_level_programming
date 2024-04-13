#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def main(argv):
    """Main function"""

    if len(argv) != 4:
        """Check for the number of command line arguments"""
        sys.exit(1)

    try:
        data = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])

        cursor = data.cursor()
        """Creating a cursor object"""

        query = "SELECT cities.id, cities.name, states.name " \
                "FROM cities " \
                "INNER JOIN states ON states.id = cities.state_id " \
                "ORDER BY cities.id ASC;"
        """The query to select"""

        cursor.execute(query)
        """Query execution"""

        rows = cursor.fetchall()
        """Fetch all the rows"""

        for row in rows:
            """Printing all rows"""
            print(row)

    except MySQLdb.Error as e:
        sys.exit(1)

    finally:
        """Closing cursor and connection for cleanup"""
        if 'cursor' in locals():
            cursor.close()
        if 'data' in locals():
            data.close()


if __name__ == "__main__":
    main(sys.argv)

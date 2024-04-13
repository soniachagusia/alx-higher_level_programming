#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def main(argv):
    """Main function"""

    if len(argv) != 5:
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

        query = "SELECT cities.name " \
                "FROM cities " \
                "INNER JOIN states ON states.id = cities.state_id " \
                "WHERE states.name = %s " \
                "ORDER BY cities.id ASC;"
        """The query to select"""

        cursor.execute(query, (argv[4],))
        """Query execution"""

        rows = cursor.fetchall()
        """Fetch all the rows"""

        cities = [row[0] for row in rows]
        """Extract city names"""

        print(", ".join(cities))

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

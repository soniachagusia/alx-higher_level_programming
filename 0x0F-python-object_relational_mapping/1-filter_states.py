#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def main(argv):
    """main function"""

    if len(sys.argv) != 4:
        """check for no of command lin args"""
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    """ command line Args for MySQL credentials """
    try:
        data = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=database)

        cursor = data.cursor()
        """creating a cursor object"""

        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
        """the query to select"""

        cursor.execute(query)
        """query execution"""

        rows = cursor.fetchall()
        """fetch all the rows """

        for row in rows:
            """printing all rows"""
            if row[1][0] == 'N':
                print(row)

    except MySQLdb.Error as e:
        sys.exit(1)

    finally:
        """closing cursor and connection for cleanup"""
        if 'cursor' in locals():
            cursor.close()
        if 'data' in locals():
            data.close()


if __name__ == "__main__":
    main(sys.argv)

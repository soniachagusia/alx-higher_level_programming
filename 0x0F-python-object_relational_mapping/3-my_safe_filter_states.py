#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def main(argv):
    """main function"""

    if len(sys.argv) != 5:
        """check for no of command line args"""
        sys.exit(1)

    try:
        data = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])

        cursor = data.cursor()
        """creating a cursor object"""

        query = "SELECT * FROM states WHERE name = %s"
        """the query to select"""

        cursor.execute(query, (argv[4],))
        """query execution"""

        rows = cursor.fetchall()
        """fetch all the rows """

        for row in rows:
            """printing all rows"""
            if row[1] == argv[4]:
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

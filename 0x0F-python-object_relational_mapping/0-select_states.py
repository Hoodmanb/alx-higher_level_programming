#!/usr/bin/python3
"""
take 3 arguments with no validation
and lists all states from the database
"""
import sys
import MySQLdb


def main(argv):
    """link all the 3 arguments to something"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(sys.argv)

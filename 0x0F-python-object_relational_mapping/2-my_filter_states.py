#!/usr/bin/python3
"""
accepts 3 arguments (mysql username, password and database name)
and lists all states from that database whose names start with a given string
"""
import sys
import MySQLdb


def main(argv):
    """display the name that matches the 4th argument"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
            "ORDER BY id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    pass
    cur.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        main(sys.argv)

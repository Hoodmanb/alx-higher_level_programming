#!/usr/bin/python3
"""
takes 4 arguments with no validation
lists all the values in the sates with a matching name 
which is safe from sql injections
"""
import sys
import MySQLdb


def main(argv):
    """display a matching name with the fours argument"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    fourth_arg = MySQLdb.escape_string(argv[4]).decode()
    cur.execute("SELECT * FROM states  WHERE name LIKE BINARY '{}%' ORDER BY id ASC".format(fourth_arg))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        main(sys.argv)

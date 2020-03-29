#!/usr/bin/python3
"""Filter states"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[2],
                         passwd=sys.argv[1],
                         db=sys.argv[3])

    cur = db.cursor()

    # Execute the query
    cur.execute('SELECT id, name FROM states\
    WHERE name COLLATE latin1_general_cs LIKE "N%" ORDER BY states.id ASC;')

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

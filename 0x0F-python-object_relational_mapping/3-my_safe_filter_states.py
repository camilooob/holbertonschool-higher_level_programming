#!/usr/bin/python3
"""SQL Injection"""
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
    query = """SELECT id, name FROM states WHERE name = %s\
    COLLATE latin1_general_cs ORDER BY id ASC;"""
    cur.execute(query, (sys.argv[4], ))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

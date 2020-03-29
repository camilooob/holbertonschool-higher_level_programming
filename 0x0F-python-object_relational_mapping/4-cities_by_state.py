#!/usr/bin/python3
"""All cities by state"""
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
    query = """
    SELECT cities.id, cities.name, states.name
    FROM states
    JOIN cities ON cities.state_id=states.id
    ORDER BY cities.id ASC;
    """
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

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
    SELECT cities.name
    FROM cities
    JOIN states ON states.id = cities.state_id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    cur.execute(query, (sys.argv[4], ))

    my_list = []
    str1 = ""
    for row in cur.fetchall():
        my_list.append(row[0])

    for i in range(len(my_list)):
        if i == len(my_list) - 1:
            str1 += my_list[i]
        else:
            str1 += "{}, ".format(my_list[i])

    print(str1)

    # Close the connection
    cur.close()
    db.close()

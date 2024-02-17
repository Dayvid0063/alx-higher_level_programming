#!/usr/bin/python3
"""Lists all cities of a specific state from the database hbtn_0e_4_usa"""


import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name=%s ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cur.fetchall()

    for res in rows:
        print(res)

    cur.close()
    conn.close()

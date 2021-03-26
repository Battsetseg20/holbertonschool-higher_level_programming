#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa:
    - Take 4 arguments: mysql username, mysql password, database name, and state name searched (safe from MySQL injection)
    - Connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
    - Your code should not be executed when imported
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db=MySQLdb.connect(host='localhost', port=3306,
                       user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
    FROM states \
    WHERE name = %s \
    ORDER BY states.id",(argv[4],))
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()

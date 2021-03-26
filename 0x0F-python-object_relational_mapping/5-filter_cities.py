#!/usr/bin/python3
""" Write a script that lists all cities from the database hbtn_0e_4_usa
    - Take 3 arguments: mysql username, mysql password and database name
    - Connect to a MySQL server running on localhost at port 3306
    - Use only execute() once
    - Results must be sorted in ascending order by cities.id
    - Your code should not be executed when imported
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db=MySQLdb.connect(host='localhost', port=3306,
                       user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.name \
    FROM cities as c \
    INNER JOIN states as s \
    ON c.state_id = s.id \
    WHERE s.name = %s \
    ORDER BY c.id",(argv[4],))
    rows = cur.fetchall()
    print('{}'.format(", ".join([row[0] for row in rows])))
    cur.close()
    db.close()

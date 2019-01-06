#!/usr/bin/python3
'''Displays all values in the states table of hbtn_0e_0_usa where the name
matches the argument, and also prevents SQL injection'''
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name =%s ORDER BY id ASC", (sys.argv[4],))

    result = cur.fetchall()
    for row in result:
        print(row)

    cur.close()
    db.close()

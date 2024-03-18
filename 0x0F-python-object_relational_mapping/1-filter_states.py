#!/usr/bin/python3
"""
decription of the task
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    curr = db.cursor()
    curr.execute("""SELECT * FROM states WHERE name 
                 LIKE 'N%' ORDER BY states.id ASC""")
    elements = curr.fetchall()
    for element in curr.elements:
        print(element)
    curr.close()
    db.close()

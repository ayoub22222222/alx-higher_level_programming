#!/usr/bin/python3
"""
this file is connecting us to database
and fetchall the states element
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host= "localhost",
            port=3306, 
            user=argv[1], 
            passwd=argv[2], 
            db=argv[3])

    curr = db.cursor()

    curr.execute("SELECT * FROM states")
    for i in curr.fetchall():
        print(i)
    curr.close()
    db.close()

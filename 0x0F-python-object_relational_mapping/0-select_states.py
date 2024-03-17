#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host= "localhost",
            port=3306, 
            user=argv[1], 
            passwd=argv[2], 
            db=argv[3])

    curr = db.cursor()

    curr.execute("SELECT * FROM states ORDER BY id ASC")
    for i in curr.fetchall():
        print(i)

    curr.close()
    db.close()

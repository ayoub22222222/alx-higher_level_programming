#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":

    in_put = sys.argv
    db = MySQLdb.connect(host= "localhost",
            port=3306, 
            user=in_put[1], 
            passwd=in_put[2], 
            db=in_put[3])

    curr = db.cursor()

    curr.execute('SELECT * FROM states ORDER BY id ASC')
    for i in curr.fetchall():
        print(i)

    curr.close()
    db.close()

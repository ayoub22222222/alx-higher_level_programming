#!/usr/bin/python3
"""
this file is connecting us to database
and fetchall the states element
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
                        
    in_put = sys.argv
    db = MySQLdb.connect(host= "localhost",
            port=3306, 
            user=in_put[1], 
            passwd=in_put[2], 
            db=in_put[3])

    curr = db.cursor()

    curr.execute("SELECT * FROM states ORDER BY states.id ASC")
    for i in curr.fetchall():
        print(i)
    curr.close()
    db.close()

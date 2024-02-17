#!/usr/bin/python3
""""Module that lists all states from the hbtn_0e_0_usa database With N in the beggining."""
import sys
import MySQLdb

if __name__ == "__main__":
    #Get MySQL credentials as cmd arguments
    #Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    #execute Query and sort by id.
    c.execute("SELECT * FROM states ORDER BY id")
    rows = c.fetchall()
    [print(row) for row in rows if row[1][0] == "N"]
    db.close()




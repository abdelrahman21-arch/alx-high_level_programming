#!/usr/bin/python3
"""This module lists all states in a database."""
import sys
import MySQLdb

if __name__ == "__main__":
    # connect to sql Db
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
    

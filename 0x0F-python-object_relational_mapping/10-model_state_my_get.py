#!/usr/bin/python3
"""This module Lists the State object with the name passed as argument from the Db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    #Create engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    #Create session
    Session = sessionmaker(bind=engine)
    #Get session obj
    session = Session()

    found = False
    # loop till found is set to True
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break
    if found is False:
        print("Not found")

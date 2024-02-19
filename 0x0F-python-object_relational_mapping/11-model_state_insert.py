#!/usr/bin/python3
"""This module Adds the State object "Louisiana" to the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    #Create engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create and bind a session
    Session = sessionmaker(bind=engine)
    session = Session()

    #send lousiana via orm as sql query to db
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    #print the result
    print(louisiana.id)

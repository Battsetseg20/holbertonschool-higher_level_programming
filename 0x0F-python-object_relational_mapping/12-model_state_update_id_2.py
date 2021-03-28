#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa using SQLAlchemy
    - Take 3 arguments: mysql username, mysql password and database name
    - You must import State and Base from model_state
    - Connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
    - Your code should not be executed when imported
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # an Engine, which the Session will use for connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
# create a configured "Session" class
Session = sessionmaker(bind=engine)
# create a Session
session = Session()
# work with session
state = session.query(State).filter_by(id=2).first()
state.name = "New Mexico"
session.commit()
# close the session
session.close()

#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_14_usa using SQLAlchemy
    - Take 3 arguments: mysql username, mysql password and database name
    - You must import State and Base from model_state
    - Connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by cities.id
    - Result format :<state name>: (<city id>) <city name>)
    - Your code should not be executed when imported
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # an Engine, which the Session will use for connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    # work with session
    for city, state in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    # close the session
    session.close()

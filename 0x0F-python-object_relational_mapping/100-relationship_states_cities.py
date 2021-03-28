#!/usr/bin/python3
"""Creates the State “California” with the City “San Francisco” from db
    - Take 3 arguments: mysql username, mysql password and database name
    - You must import State and Base from model_state
    - Connect to a MySQL server running on localhost at port 3306
    - You must use the cities relationship for all State Objects
    - Your code should not be executed when imported
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    # an Engine, which the Session will use for connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)
# create a configured "Session" class
Session = sessionmaker(bind=engine)
# create a Session
session = Session()
# work with session
session.add(City(name="San Francisco", state=State(name="California")))
session.commit()
# close the session
session.close()

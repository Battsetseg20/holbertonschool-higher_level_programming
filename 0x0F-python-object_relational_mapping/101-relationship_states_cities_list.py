#!/usr/bin/python3

"""
Lists all State objects, and corresponding City objects, in db hbtn_0e_101_usa
    - take 3 arguments: mysql username, mysql password, and database name
    - Use the module SQLAlchemy
    - connect the MySQL server must be to localhost on port 3306
    - You must use the cities relationship for all State objects
    - Results must be sorted in ascending order by states.id and cities.id
    - Result format: <state id>: <state name>
                     <tabulation><city id>: <city name>
    - Code should not be executed when imported
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    # Engine to use for connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create a configured "Session" class: bind is used to access database
    Session = sessionmaker(bind=engine)

    # creata a Session
    session = Session()

    # work with the session
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

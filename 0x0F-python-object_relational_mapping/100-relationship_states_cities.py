#!/usr/bin/python3
"""script that creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import exit, argv
from relationship_state import Base, State
from urllib.parse import quote_plus
from relationship_city import City


if __name__ == "__main__":
    """ creates the State “California” with
        the City “San Francisco” from db"""
    if (len(argv) < 4):
        exit(1)

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    passwd_escaped = quote_plus(passwd)  # filterd/escaped special char '@'

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{\
}".format(user, passwd_escaped, db))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
    session.close()

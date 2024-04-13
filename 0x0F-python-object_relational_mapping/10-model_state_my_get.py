#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database)
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (
        session.query(State)
        .filter(State.name == state_name)
        .first()
    )

    if state:
        print(state.id)
    else:
        print("Not found")

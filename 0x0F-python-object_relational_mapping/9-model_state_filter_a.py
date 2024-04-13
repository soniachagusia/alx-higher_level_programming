#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database)
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = (
        session.query(State)
        .filter(State.name.ilike('%a%'))
        .order_by(State.id)
        .all()
    )

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

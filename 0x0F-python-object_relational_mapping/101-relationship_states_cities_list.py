#!/usr/bin/python3
"""creates a state 'california' and a city 'san francisco' in the database"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":

    username, password, database = argv[1], argv[2], argv[3]
    host = "localhost"
    port = "3306"
    mysql_url = f"mysql+mysqldb://{username}:{password}@{host}:\
        {port}/{database}"
    engine = create_engine(mysql_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        query = session.query(State).order_by(State.id).all()

        for state in query:
            print(f"{state.id}: {state.name}")

            for city in state.cities:
                print(f"    {city.id}: {city.name}")

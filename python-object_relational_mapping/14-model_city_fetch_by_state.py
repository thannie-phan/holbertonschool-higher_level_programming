#!/usr/bin/python3
"""print all City objects from the database hbnt_0e_14_usa"""

import MySQLdb
import sys
from sqlalchemy import Column, Integer, String, create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    all_cities = (
        session.query(City)
        .order_by(City.id)
        .all()
    )

    for cities in all_cities:
        print(f"{cities.state.name}: ({cities.id}) {cities.name}")

    session.close()

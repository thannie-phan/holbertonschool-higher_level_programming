#!/usr/bin/python3
"""prints the State object with the name passed as argument """

import MySQLdb
import sys
from sqlalchemy import Column, Integer, String, create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = (
        session.query(State)
        .filter(State.id == 2)
        .first()
    )

    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()

    session.close()

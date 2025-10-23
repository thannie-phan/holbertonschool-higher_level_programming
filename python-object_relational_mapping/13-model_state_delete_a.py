#!/usr/bin/python3
"""Defines State class and creates states table in MySQL"""

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

    state_to_delete = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
    )

    for state in state_to_delete:
        session.delete(state)

    session.commit()

    session.close()

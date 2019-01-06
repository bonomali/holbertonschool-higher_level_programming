#!/usr/bin/python3
'''lists all State objects from the database hbtn_0e_6_usa'''

from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    sess = session()

    for state in sess.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    sess.close

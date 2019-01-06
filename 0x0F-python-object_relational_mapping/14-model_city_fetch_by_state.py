#!/usr/bin/python3
'''Prints all City objects  from the database hbtn_0e_14_usa'''

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    sess = session()

    query = sess.query(City, State).filter(State.id == City.state_id).order_by(City.id)
    for city, states in query:
        print("{}: ({}) {}".format(states.name, city.id, city.name))

    sess.close

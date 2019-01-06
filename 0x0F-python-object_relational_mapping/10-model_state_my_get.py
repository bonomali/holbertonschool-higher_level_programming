#!/usr/bin/python3
'''Prints the State object with the name passed as argument from the database
hbtn_0e_6_usa'''

from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    sess = session()

    state = sess.query(State).filter(State.name == sys.argv[4]).all()
    if state:
        for item in state:
            print("{}".format(item.id))
    else:
        print("Not Found")

    sess.close

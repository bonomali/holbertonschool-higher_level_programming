#!/usr/bin/python3
'''Adds the State object Louisiana to the database hbtn_0e_6_usa'''

from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    sess = session()

    new = State(name="Louisiana")
    sess.add(new)
    sess.commit()
    print('{}'.format(new.id))

    sess.close

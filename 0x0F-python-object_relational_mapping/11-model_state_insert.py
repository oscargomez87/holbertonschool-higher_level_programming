#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

from model_state import Base, State
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """main method for model"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3],
                                   pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    n_state = State(name='Louisiana')
    session.add(n_state)
    session.commit()
    print(n_state.id)


if __name__ == "__main__":
    main()

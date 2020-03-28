#!/usr/bin/python3
"""Prints the State object with the name
passed as argument from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """main method of module"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3],
                                   pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == argv[4]).one_or_none()
    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    main()

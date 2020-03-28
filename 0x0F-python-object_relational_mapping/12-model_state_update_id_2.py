#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """main method for module"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3],
                                   pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    u_state = session.query(State).filter(State.id == '2').first()
    u_state.name = 'New Mexico'
    session.commit()

if __name__ == "__main__":
    main()

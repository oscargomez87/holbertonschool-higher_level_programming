#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

from model_city import Base, City, State
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
    for instance in session.query(City).join(State).order_by(City.id).all():
        print("{}: ({}) {}"
              .format(instance.state.name, instance.id, instance.name))


if __name__ == "__main__":
    main()

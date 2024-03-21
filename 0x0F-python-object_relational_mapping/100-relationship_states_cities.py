#!/usr/bin/python3
"""ths is for descriptin"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    
    cn_db = 'mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(cn_db, pool_pre_ping=True)

    Base.metadata.cerate_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    n_state = State(name='California')
    n_city = Cityname='San Francisco')
    n_state.cities.append(n_city)

    session.add(n_state)
    session.add(n_city)
    session.commit()


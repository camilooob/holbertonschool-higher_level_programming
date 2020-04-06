#!/usr/bin/python3
"""Start link class to table in database
"""
if __name__ == '__main__':
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    sql_username = sys.argv[1]
    sql_pwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sql_username, sql_pwd, db_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = "California"
    new_city = "San Francisco"

    n_state = State(name=new_state)
    session.add(n_state)
    session.commit()

    n_city = City(name=new_city, state=n_state)
    session.add(n_city)
    session.commit()

    session.close()

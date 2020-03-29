#!/usr/bin/python3
"""Start link class to table in database
"""
if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    sql_username = sys.argv[1]
    sql_pwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sql_username, sql_pwd, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).join(City).order_by(City.id).all()
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

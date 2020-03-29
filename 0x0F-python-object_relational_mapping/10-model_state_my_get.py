#!/usr/bin/python3
"""
Get state id
"""
if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    sql_username = sys.argv[1]
    sql_pwd = sys.argv[2]
    db_name = sys.argv[3]
    f_state = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sql_username, sql_pwd, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == f_state).all()

    if query:
        for state in query:
            print(state.id)
    else:
        print("Not found")

    session.close()

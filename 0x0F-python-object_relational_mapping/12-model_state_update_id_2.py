#!/usr/bin/python3
"""
Update the table
"""
if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    sql_username = sys.argv[1]
    sql_pwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sql_username, sql_pwd, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter_by(id=2)
    query.update({State.name: "New Mexico"}, synchronize_session=False)
    session.commit()

    session.close()

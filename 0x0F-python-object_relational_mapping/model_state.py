#!/usr/bin/python3
"""Module for states table"""
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """A class for state"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """Object Representation"""
        return "<States(name =' %s')>" % (self.name)

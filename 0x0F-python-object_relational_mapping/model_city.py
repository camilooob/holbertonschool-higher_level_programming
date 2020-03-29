#!/usr/bin/python3
"""MOduke for citiess table"""
from model_state import Base, State
from sqlalchemy import ForeignKey, Column, Integer, String


class City(Base):
    """The city class for this table"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    def __repr__(self):
        """Object Representation"""
        return "<Cities(name =' %s')>" % (self.name)

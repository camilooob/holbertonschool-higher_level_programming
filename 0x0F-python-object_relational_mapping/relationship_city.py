#!/usr/bin/python3
"""adv 101"""
from relationship_state import Base, State
from sqlalchemy import ForeignKey, Column, Integer, String


class City(Base):
    """The city class for this table"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

#!/usr/bin/python3
"""description file"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


mt = MetaData()
Base = declarative_base(mt)


class State(Base):
    """description of the class"""
    __tablename__ = 'states'
    id = column(Integer, unique=True, nullable=False, primary_key=True)
    name = column(String(128), nullable=False)

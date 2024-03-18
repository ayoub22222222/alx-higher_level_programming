#!/usr/bin/python3
"""description file that link an object class to data base using sqlalchemy"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


mt = MetaData()
Base = declarative_base(metadata=mt)


class State(Base):
    """description of the class"""
    __tablename__ = 'states'
    id = column(Integer, unique=True, nullable=False, primary_key=True)
    name = column(String(128), nullable=False)

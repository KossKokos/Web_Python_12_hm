from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(60), nullable=False)
    email = Column(String(30), nullable=False)
    phone_number = Column(String(20), nullable=False)
    birth_date = Column(Date, nullable=False)
    description = Column(String(300), nullable=True)
    user_id = Column('user_id', ForeignKey('users.id', ondelete='CASCADE'), default=None)
    user = relationship('User', backref='contacts')
    


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(200), nullable=False)
    refresh_token = Column(String(300), nullable=True)

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorite(Base):
    __tablename__ = 'favorite'
    favoriteID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('user.UserID'))
    characterID =Column(Integer, ForeignKey('character.CharacterID'))

class Character(Base):
    __tablename__ = 'character'
    CharacterID = Column(Integer, primary_key=True)
    Name = Column(String(40), nullable=False)
    Episode = Column(String(40), nullable=True)
    FavoriteID = relationship('Favorite')
    LocationID = relationship('Location')
    StatusID = relationship('Status')
    
class Status(Base):
    __tablename__ = 'status'
    StatusID = Column(Integer, ForeignKey('character.StatusID'), primary_key=True)
    Status = Column(String(15), nullable=True)

class User(Base):
    __tablename__ = 'user'
    UserID = Column(Integer, primary_key=True)
    Name = Column(String(40), nullable=False, unique=True)
    Password = Column(String(20), nullable=False)
    Email = Column(String(60), nullable=False, unique=True)
    favoriteID = relationship('Favorite')

class Location(Base):
    __tablename__ = 'location'
    LocationID = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    characterID = Column(Integer, ForeignKey('character.CharacterID'))

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

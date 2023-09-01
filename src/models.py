import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorite(Base):
    __tablename__ = 'favorite'
    FavoriteID = Column(Integer, ForeignKey('character.CharacterID'), primary_key=True)
    UserID = Column(Integer, ForeignKey('user.UserID'))

class Character(Base):
    __tablename__ = 'character'
    CharacterID = Column(Integer, relationship(Favorite, Location), primary_key=True)
    Name = Column(String(40), nullable=False)
    Location = Column(String(40), nullable=False)
    Episode = Column(String(40), nullable=True)
    Status =  Column(Integer, nullable=False)
    StatusID = Column(Integer, relationship(Status))
    

class Status(Base):
    __tablename__ = 'status'
    StatusID = Column(Integer, ForeignKey('character.StatusID'), primary_key=True)


class User(Base):
    __tablename__ = 'user'
    UserID = Column(Integer, relationship(Favorite), primary_key=True)
    Name = Column(String(40), nullable=False, unique=True)
    Password = Column(String(20), nullable=False)
    Email = Column(String(60), nullable=False, unique=True)


class Location(Base):
    __tablename__ = 'location'
    LocationID = Column(Integer, ForeignKey('character.CharacterID'), primary_key=True)



# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

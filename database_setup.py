import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


'''This file creates a database with 4 tables: 
restaurant, menu_item, employee and address'''
class Restaurant(Base):
    '''Setting up Restaurant Table'''
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class MenuItem(Base):
    '''Setting up Menu table'''
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    # This allows us to send JSON objects in a serializable format
    @property
    def serialize(self):
        """Returns object data in easily serializable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }   

class Employee(Base):
    __tablename__ = 'employee'
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)


class Address(Base):
    __tablename__ = 'address'
    street = Column(String(80), nullable = False)
    zip = Column(String(5), nullable = False)
    id = Column(Integer, primary_key = True)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship(Employee)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)

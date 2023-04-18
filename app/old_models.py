# Import Any Additional sqlalchemy types here
from sqlalchemy import Column, Integer, String, Time, ForeignKey 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Models:
# class Model(Base):
#   __tablename__ = "models"
#   __table_arge__ = (TableArgsAsTuple)
#   
#   Setup Columns and DataTypes
#   
#   Setup Relationships
# 
#   Optional:
#   def __repr__(self): 
#     return "A Better Print Output"

class Airline(Base):
    __tablename__ = "airlines"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
    flights = relationship("Flight", backref=backref("airline"))

    def __repr__(self):
        return f"Airline: {self.name} (ID: {self.id})"
    

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer(), primary_key=True)
    flight_number = Column(Integer())
    destination = Column(String())
    departure_time = Column(Time())
    gate = Column(String())
    airline_id = Column(Integer(), ForeignKey("airlines.id"))

    def __repr__(self):
        return f"Flight Number:\t{self.flight_number}" \
            f"Destination:\t{self.destination}" \
            f"Departure Time:\t{self.departure_time}" \
            f"Departure Gate:\t{self.gate}"


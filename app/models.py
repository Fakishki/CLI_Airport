# Import Any Additional sqlalchemy types here
from sqlalchemy import Column, Integer, String, Time, ForeignKey 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Airline(Base):
    __tablename__ = "airlines"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
    flights = relationship("Flight", back_populates="airline")

    def __repr__(self):
        return f"Airline: {self.name} (ID: {self.id})"
    

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer(), primary_key=True)
    flight_number = Column(Integer())
    destination = Column(String())
    departure_time = Column(String())
    gate = Column(String())
    airline_id = Column(Integer(), ForeignKey("airlines.id"))

    airline = relationship("Airline", back_populates="flights")
    passengers = relationship("Passenger", back_populates="flight")

    def __repr__(self):
        return f"Airline:\t{self.airline.name}\n" \
            f"Flight Number:\t{self.flight_number}\n" \
            f"Destination:\t{self.destination}\n" \
            f"Departure Time:\t{self.departure_time}\n" \
            f"Departure Gate:\t{self.gate}"


class Passenger(Base):
    __tablename__ = "passengers"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    flight_id = Column(Integer(), ForeignKey("flights.id"))

    flight = relationship("Flight", back_populates="passengers")

    def __repr__(self):
        return f"Passenger: {self.name} <Flight: {self.flight.airline.name} {self.flight.flight_number}>"
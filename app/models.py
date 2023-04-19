# Import Any Additional sqlalchemy types here
from sqlalchemy import Column, Integer, String, Time, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time

engine = create_engine('sqlite:///development.db')
session = sessionmaker(bind=engine)()

Base = declarative_base()

class Airline(Base):
    __tablename__ = "airlines"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
    flights = relationship("Flight", back_populates="airline")

    def __repr__(self):
        output = f"Airline: {self.name} (ID: {self.id})"
        words = output.split()
        for word in words:
            for char in word:
                print(char, end='', flush=True)
                if char != ' ':
                    time.sleep(0.009)
            print(' ', end='', flush=True)
        print()
        return ""

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
        output = f"Airline:\t{self.airline.name}\n" \
            f"Flight Number:\t{self.flight_number}\n" \
            f"Destination:\t{self.destination}\n" \
            f"Departure:\t{self.departure_time}\t"f"Gate:\t{self.gate}"
        lines = output.split('\n')
        for line in lines:
            for char in line:
                print(char, end='', flush=True)
                if char != ' ':
                    time.sleep(0.009)
            print('\n', end='', flush=True)
        return ""



class Passenger(Base):
    __tablename__ = "passengers"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    flight_id = Column(Integer(), ForeignKey("flights.id"))

    flight = relationship("Flight", back_populates="passengers")
    bags = relationship("Bag", back_populates="passenger")

    def __repr__(self):
        if self.flight_id is not None:
            flight = session.query(Flight).filter(Flight.id == self.flight_id).first()
            output = f"Passenger {self.id}: {self.name} <Flight: {flight.airline.name} {flight.flight_number}>"
        else:
            output = f"Passenger {self.id}: {self.name} <Flight: None>"
        words = output.split()
        for word in words:
            for char in word:
                print(char, end='', flush=True)
                if char != ' ':
                    time.sleep(0.004)
            print(' ', end='', flush=True)
        print()
        return ""

class Bag(Base):
    __tablename__ = "bags"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    passenger_id = Column(Integer(), ForeignKey("passengers.id"))

    passenger = relationship("Passenger", back_populates="bags")

    def __repr__(self):
        if self.passenger.flight_id is not None:
            passenger = session.query(Passenger).filter(Passenger.id == self.passenger_id).first()
            output = f"Bag Tag: {self.id} [{self.name}] Owner: {passenger.name} <Flight: {passenger.flight.airline.name} {passenger.flight.flight_number}>"
        else:
            output = f"Bag Tag: {self.id} [{self.name}] Owner: {self.passenger.name} <Flight: None>"
        words = output.split()
        for word in words:
            for char in word:
                print(char, end='', flush=True)
                if char != ' ':
                    time.sleep(0.004)
            print(' ', end='', flush=True)
        print()
        return ""
from ipdb import set_trace
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Airline, Flight, Passenger

engine = create_engine('sqlite:///development.db')
session = sessionmaker(bind=engine)()

all_airlines = session.query(Airline).all()
all_flights = session.query(Flight).all()
all_passengers = session.query(Passenger).all()

def show_all_flights(flights):
    for flight in flights:
        print("-" * 32)
        print(flight)
        print("-" * 32)


from ipdb import set_trace
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

from models import Airline, Flight, Passenger

engine = create_engine('sqlite:///development.db')
session = sessionmaker(bind=engine)()

all_airlines = session.query(Airline).all()
all_flights = session.query(Flight).all()
all_passengers = session.query(Passenger).all()

def print_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def print_kinda_slow(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.008)
    print()

def show_all_flights(flights):
    for flight in flights:
        print("-" * 32)
        print(flight)

def show_all_airlines(airlines):
    for airline in airlines:
        print("-" * 32)
        print(airline)

def show_all_passengers(passengers):
    for passenger in passengers:
        print(passenger)

greeting_image = """
         ___________                |
        |CLI Airport|               |
         ```````````                |
                                  .-'-.
                                 ' ___ '
                       ---------'  .-.  '---------
       _________________________'  '-'  '_________________________
        ''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-''''''
                      \    /  ||/   H   \||  \    /
                       '--'   OO   O|O   OO   '--'
"""
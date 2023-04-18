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
booked_passengers = [passenger for passenger in all_passengers if passenger.flight_id is not None]
awaiting_passengers = [passenger for passenger in all_passengers if passenger.flight_id is None]

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

def print_rapidly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.004)
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

def passenger_menu():
    while True:
        print_slowly("*" * 10 + " Passengers menu " + "*" * 10)
        print_slowly("Select an option")
        print_slowly("List => \tList all passengers")
        print_slowly("Booked => \tList passengers currently booked on a flight")
        print_slowly("Awaiting => \tList passengers not booked on a flight")
        print_slowly("Exit => \tGo back to the Main Menu")
        print_slowly("*" * 37)
        print_slowly("Enter your command:")
        passenger_input = input()
        result = passenger_command(passenger_input)
        if result == "exit":
            break

def passenger_command(user_input):
    if user_input.lower() == "list":
        print_slowly("*" * 10 + " All Passengers " + "*" * 10)
        show_all_passengers(all_passengers)
    elif user_input.lower() == "booked":
        print_slowly("*" * 10 + " Booked Passengers " + "*" * 10)
        show_all_passengers(booked_passengers)
    elif user_input.lower() == "awaiting":
        print_slowly("*" * 10 + " Passengers Awaiting Flights " + "*" * 10)
        show_all_passengers(awaiting_passengers)
    elif user_input.lower() == "exit":
        return "exit"
    else:
        print_slowly("Invalid command. Please try again or type 'exit' to return to the main menu:")

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
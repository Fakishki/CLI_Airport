from ipdb import set_trace
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased
import time

from models import Airline, Flight, Passenger, Bag

engine = create_engine('sqlite:///development.db')
session = sessionmaker(bind=engine)()

all_flights = session.query(Flight).all()

def print_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.02)
        # time.sleep(0)
    print()

def print_kinda_slow(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.008)
        # time.sleep(0)
    print()

def print_rapidly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.004)
        # time.sleep(0)
    print()

def show_all_flights(flights):
    for flight in flights:
        print("-" * 32)
        print(flight)

def show_all_airlines(airlines):
    for airline in airlines:
        print("-" * 32)
        print(airline)

def show_all_passengers():
    all_passengers = session.query(Passenger).all()
    for passenger in all_passengers:
        print(passenger)

def show_awaiting_passengers():
    awaiting_passengers = session.query(Passenger).filter_by(flight_id = None).all()
    for passenger in awaiting_passengers:
        print(passenger)

def show_booked_passengers():
    booked_passengers = session.query(Passenger).filter(Passenger.flight_id != None).all()
    for passenger in booked_passengers:
        print(passenger)

def show_all_bags_by_tag():
    all_bags = session.query(Bag).order_by(Bag.name).all()
    for bag in all_bags:
        print(bag)

def show_all_bags_by_passenger():
    PassengerAlias = aliased(Passenger)
    all_bags = session.query(Bag).join(PassengerAlias, Bag.passenger_id == PassengerAlias.id).order_by(PassengerAlias.name).all()
    for bag in all_bags:
        print(bag)

def passenger_menu():
    while True:
        print_slowly("*" * 10 + " Passengers menu " + "*" * 10)
        print_slowly("Select an option")
        print_slowly("All => \t\tList all passengers")
        print_slowly("Booked => \tList passengers currently booked on a flight")
        print_slowly("Awaiting => \tList passengers not booked on a flight")
        print_slowly("Exit => \tGo back to the Main Menu")
        print_slowly("*" * 37)
        print_slowly("Enter your command:")
        passenger_input = input()
        result = passenger_command(passenger_input)
        if result == "exit":
            break

def book_passenger(passenger_id):
    awaiting_passengers = session.query(Passenger).filter_by(flight_id=None).all()
    valid_ids = [passenger.id for passenger in awaiting_passengers]

    try:
        passenger_id_int = int(passenger_id)
    except ValueError:
        print_slowly("Hey now! That's not even an integer. Let's step back here a moment...")
        return

    if passenger_id_int not in valid_ids:
        print_slowly("Whoa there! That's not a valid passenger ID. Let's step back here a moment...")
        return
    
    print_slowly("Here are the available flights:")
    print_slowly("~" * 40)
    show_all_flights(all_flights)
    print_slowly("~" * 40)
    print_slowly("Enter the flight number to book the passenger on:")
    flight_input = input()

    try:
        flight_input_int = int(flight_input)
    except ValueError:
        print_slowly("Now you're just being silly. That's not a valid flight number. Let's try this again.")
        return
    
    selected_flight = session.query(Flight).filter(Flight.flight_number == int(flight_input)).first()
    if selected_flight:
        passenger = session.query(Passenger).filter(Passenger.id == int(passenger_id)).first()
        passenger.flight_id = selected_flight.id
        session.commit()
        print_slowly(f"Passenger {passenger.name} has been booked on {selected_flight.airline.name} Flight {selected_flight.flight_number}.")
    else:
        print_slowly("Invalid flight number. That's okay. Let's start over.")

def re_book_passenger(passenger_id):
    booked_passengers = session.query(Passenger).filter(Passenger.flight_id != None).all()
    valid_ids = [passenger.id for passenger in booked_passengers]

    try:
        passenger_id_int = int(passenger_id)
    except ValueError:
        print_slowly("Hey now! That's not even an integer. Let's step back here a moment...")
        return

    if passenger_id_int not in valid_ids:
        print_slowly("Whoa there! That's not a valid passenger ID. Let's step back here a moment...")
        return
    
    print_slowly("Here are the available flights:")
    print_slowly("~" * 40)
    show_all_flights(all_flights)
    print_slowly("~" * 40)
    print_slowly("Enter the flight number to book the passenger on:")
    flight_input = input()

    try:
        flight_input_int = int(flight_input)
    except ValueError:
        print_slowly("Now you're just being silly. That's not a valid flight number. Let's try this again.")
        return
    
    selected_flight = session.query(Flight).filter(Flight.flight_number == int(flight_input)).first()
    if selected_flight:
        passenger = session.query(Passenger).filter(Passenger.id == int(passenger_id)).first()
        passenger.flight_id = selected_flight.id
        session.commit()
        print_slowly(f"Passenger {passenger.name} has been rebooked on {selected_flight.airline.name} Flight {selected_flight.flight_number}.")
    else:
        print_slowly("Invalid flight number. That's okay. Let's start over.")

def passenger_command(user_input):
    if user_input.lower() == "all":
        print_slowly("*" * 10 + " All Passengers " + "*" * 10)
        show_all_passengers()
    elif user_input.lower() == "booked":
        print_slowly("*" * 10 + " Booked Passengers " + "*" * 10)
        show_booked_passengers()
        while True:
            print_slowly("Select an option:")
            print_slowly("1 => \tRebook a passenger on a different flight")
            print_slowly("2 => \tGo back to the passengers menu")
            print_slowly("3 => \tGo back to the main menu")
            awaiting_input = input()
            if awaiting_input == "1":
                print_slowly("Enter the passenger ID to rebook them on a flight (I sure hope they make it in time):")
                passenger_id = input()
                re_book_passenger(passenger_id)
            elif awaiting_input == "2":
                break
            elif awaiting_input == "3":
                return "exit"
            else:
                print_slowly("Invalid selection. Come on... there are only three choices.")
    elif user_input.lower() == "awaiting":
        print_slowly("*" * 10 + " Passengers Awaiting Flights " + "*" * 10)
        show_awaiting_passengers()
        while True:
            print_slowly("Select an option:")
            print_slowly("1 => \tBook a passenger on a flight")
            print_slowly("2 => \tGo back to the passengers menu")
            print_slowly("3 => \tGo back to the main menu")
            awaiting_input = input()
            if awaiting_input == "1":
                print_slowly("Enter the passenger ID to book them on a flight:")
                passenger_id = input()
                book_passenger(passenger_id)
            elif awaiting_input == "2":
                break
            elif awaiting_input == "3":
                return "exit"
            else:
                print_slowly("Invalid selection. Come on... there are only three choices.")
    elif user_input.lower() == "exit":
        return "exit"
    else:
        print_slowly("Invalid command. Please try again or type 'exit' to return to the main menu:")

def bag_menu():
    while True:
        print_slowly("*" * 10 + " Luggage Menu " + "*" * 10)
        print_slowly("To help lost luggage find its owner, select an option below:")
        print_slowly("Bag => \t\tList all luggage ordered by bag tag")
        print_slowly("Passenger => \tList all luggage ordered by passenger name")
        print_slowly("Exit => \tGo back to the Main Menu")
        print_slowly("*" * 37)
        print_slowly("Enter your command:")
        bag_input = input()
        result = bag_command(bag_input)
        if result == "exit":
            break

def bag_command(user_input):
    if user_input.lower() == "bag":
        print_slowly("*" * 10 + " Luggage listed by bag tag " + "*" * 10)
        show_all_bags_by_tag()
    elif user_input.lower() == "passenger":
        print_slowly("*" * 10 + " Luggage listed by passenger name " + "*" * 10)
        show_all_bags_by_passenger()
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
# goodbye_message = 
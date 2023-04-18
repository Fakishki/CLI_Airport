from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace

from models import Airline, Flight, Passenger
from helpers import *

engine = create_engine('sqlite:///development.db')
session = sessionmaker(bind=engine)()

all_airlines = session.query(Airline).all()
all_flights = session.query(Flight).all()
all_passengers = session.query(Passenger).all()

if __name__ == '__main__':
    print("WELCOME TO CLI AIRPORT")

    def main_menu():
        print("Select an option")
        print("1 => \tSee all flights")
        print("2 => \tSee all airlines")
        print("3 => \tSee all passengers")
        first_input = input()

        if first_input == "1":
            show_all_flights(all_flights)
            main_menu()
        elif first_input == "2":
            show_all_airlines(all_airlines)
            main_menu()
        elif first_input == "3":
            show_all_passengers(all_passengers)
            main_menu()
        else:
            print("Invalid Input")

main_menu()
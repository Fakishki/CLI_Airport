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
        first_input = input()

        if first_input == "1":
            show_all_flights(all_flights)
            main_menu()
        
        else:
            print("Invalid Input")

main_menu()
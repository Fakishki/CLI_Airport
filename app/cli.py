from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace

from models import Airline, Flight, Passenger
from helpers import *
import time

engine = create_engine('sqlite:///development.db')
session = sessionmaker(bind=engine)()

all_airlines = session.query(Airline).all()
all_flights = session.query(Flight).all()
all_passengers = session.query(Passenger).all()

if __name__ == '__main__':
    print_kinda_slow(greeting_image)
    print_slowly("WELCOME TO CLI AIRPORT FLIGHT AND PASSENGER MANAGEMENT SYSTEM")

    def main_menu():
        print_slowly("******** Main Menu ********")
        print_slowly("Select an option")
        print_slowly("1 => \tFlights")
        print_slowly("2 => \tAirlines")
        print_slowly("3 => \tPassengers")
        print_slowly("X => \tExit Application")
        print_slowly("***************************")
        first_input = input()

        if first_input == "1":
            print_slowly("********** Today's scheduled flights **********")
            show_all_flights(all_flights)
            print_slowly("Enter the flight number to see details, or type 'exit' to return to the main menu:")
            flight_input = input()
            while flight_input != "exit":
                selected_flight = session.query(Flight).filter(Flight.flight_number == int(flight_input)).first()
                if selected_flight:
                    print("******** Flight information ********")
                    print(selected_flight)
                    passengers_on_flight = session.query(Passenger).filter(Passenger.flight_id == selected_flight.id).all()
                    print("******** Passengers on this flight: ********")
                    show_all_passengers(passengers_on_flight)
                else:
                    print_slowly("Invalid flight number. Please try again or type 'exit' to return to the main menu:")
                print_slowly("Enter another flight number or type 'exit' to return to the main menu:")
                flight_input = input()
            main_menu()
        elif first_input == "2":
            print_slowly("*" * 10 + " All airlines operating at CLI " + "*" * 10)
            show_all_airlines(all_airlines)
            print_slowly("Enter the airline's ID number to see scheduled flights, or type 'exit' to return to the main menu:")
            airline_input = input()
            while airline_input != "exit":
                selected_airline = session.query(Airline).filter(Airline.id == int(airline_input)).first()
                if selected_airline:
                    print("******** Airline information ********")
                    print(selected_airline)
                    airline_flights = session.query(Flight).filter(Flight.airline_id == selected_airline.id).all()
                    print("******** Airline's scheduled flights: ********")
                    show_all_flights(airline_flights)
                else:
                    print_slowly("Invalid airline ID. Please try again or type 'exit' to return to the main menu:")
                print_slowly("Enter another airline ID number or type 'exit' to return to the main menu:")
                airline_input = input()
            main_menu()
        elif first_input == "3":
            print_slowly("*" * 10 + " All passengers " + "*" * 10)
            show_all_passengers(all_passengers)
            main_menu()
        elif first_input.lower() == "x":
            print_slowly("Thank you for visiting CLI Airport. We hope you didn't mess up anyone else's intinerary. Safe travels!")
            return
        else:
            print_slowly("Invalid Input")
            main_menu()

main_menu()
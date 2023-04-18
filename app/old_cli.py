from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace

# from models import *
# from helpers import *

engine = create_engine('sqlite:///development.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
  # Intro: welcome to the CLI, pick a store
  print("WELCOME TO YOUR CLI PROJECT!!!!")
  
  # Main Menu function 
  def main_menu():
    print("Choose an option")
    print("1")
    print("2")
    first_input = input()

    if first_input == "something":
        # Do something
        # Loop back to main_menu?
        pass
    elif first_input == "another thing":
        # Do something else
        # Loop back to main_menu?
        pass
    else: 
        print("Error")
        pass

  # Now we call the method once outside of the definition, but inside the "__main__"
  main_menu()
  # Goodbye Message
  print("Thanks for using my CLI!")
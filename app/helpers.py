from ipdb import set_trace
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from models import Model

engine = create_engine('sqlite:///development.db')
session = sessionmaker(bind=engine)()

# ! Ex Input
# input = input("What do you want?")
# => type "hello"
# print(f'You typed: {input}')
# => Output: You typed hello
# input() will always return a String!

# ! Ex Helper Method, Shows all stores in a Human Readable way
# def show_all_stores(stores):
#     for store in stores:
#         print("-" * 50)
#         print(store)
#         print("-" * 50)

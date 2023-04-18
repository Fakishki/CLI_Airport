from ipdb import set_trace
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from models import *

if __name__ == '__main__':

  print("Seeding 🌱...")
  print("Connecting to DB....")
  engine = create_engine('sqlite:///development.db')
  session = sessionmaker(bind=engine)()
  print("Session Created...")

  fake = Faker()
  
  print("Dropping DB...")

  print("CREATING Models....")

  print("DONE!")
from ipdb import set_trace
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Airline, Flight, Passenger
import random
# from base import Base, engine

if __name__ == '__main__':

  print("Seeding 🌱...")
  print("Connecting to DB....")
  engine = create_engine('sqlite:///development.db')
  Session = sessionmaker(bind=engine)
  session = Session()

  # Base.metadata.create_all()
  
  print("Session Created...")

  fake = Faker()

  def random_gate():
    capital_letter = random.choice("ABCD")
    number = random.randint(1, 9)
    return capital_letter + str(number)
  
  print("Dropping old database tables...")
  session.query(Airline).delete()
  session.query(Flight).delete()
  session.query(Passenger).delete()
  session.commit()
  print("Old Airlines, Flights, and Passengers tables deleted")

  print("Creating new Airline, Flight, and Passenger tables...")
  
  oceanic = Airline(name="Oceanic")
  ajira = Airline(name="Ajira")
  whitestar = Airline(name="White Star")
  colonial = Airline(name="Colonial Fleet")
  uga = Airline(name="United Global Alliance")

  session.add_all([oceanic, ajira, whitestar, colonial, uga])
  session.commit()
  print("Airlines established")
  o111 = Flight(airline_id=oceanic.id, flight_number=111, destination=fake.city(), departure_time="8:00", gate=random_gate())
  o123 = Flight(airline_id=oceanic.id, flight_number=123, destination=fake.city(), departure_time="9:00", gate=random_gate())
  a222 = Flight(airline_id=ajira.id, flight_number=222, destination=fake.city(), departure_time="10:00", gate=random_gate())
  a234 = Flight(airline_id=ajira.id, flight_number=234, destination=fake.city(), departure_time="11:00", gate=random_gate())
  w333 = Flight(airline_id=whitestar.id, flight_number=333, destination=fake.city(), departure_time="12:00", gate=random_gate())
  w345 = Flight(airline_id=whitestar.id, flight_number=345, destination=fake.city(), departure_time="13:00", gate=random_gate())
  c444 = Flight(airline_id=colonial.id, flight_number=444, destination=fake.city(), departure_time="14:00", gate=random_gate())
  c456 = Flight(airline_id=colonial.id, flight_number=456, destination=fake.city(), departure_time="15:00", gate=random_gate())
  u555 = Flight(airline_id=uga.id, flight_number=555, destination=fake.city(), departure_time="16:00", gate=random_gate())
  u567 = Flight(airline_id=uga.id, flight_number=567, destination=fake.city(), departure_time="17:00", gate=random_gate())

  session.add_all([o111,o123,a222,a234,w333,w345,c444,c456,u555,u567])
  session.commit()
  print("Flights scheduled")

  flights_list = [o111, o123, a222, a234, w333, w345, c444, c456, u555, u567]
  print("Flights gathered... compiling passenger lists")
  
  p01 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p02 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p03 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p04 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p05 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p06 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p07 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p08 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p09 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p10 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p11 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p12 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p13 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p14 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p15 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p16 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p17 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p18 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p19 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p20 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p21 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p22 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p23 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p24 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p25 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p26 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p27 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p28 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p29 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)
  p30 = Passenger(name=fake.name(), flight_id=random.choice(flights_list).id)

  session.add_all([p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30])
  session.commit()
  print("Passengers booked")

  print("Database Tables Created!")
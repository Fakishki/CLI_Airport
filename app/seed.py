from ipdb import set_trace
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Airline, Flight, Passenger, Bag
from helpers import *
import random, string, time
# from base import Base, engine

if __name__ == '__main__':

  print_slowly("Planting the seeds 🌱...")
  print_slowly("Connecting to DB....")
  engine = create_engine('sqlite:///development.db')
  Session = sessionmaker(bind=engine)
  session = Session()

  # Base.metadata.create_all()
  
  print_slowly("Session Created...")

  fake = Faker()

  def random_gate():
    capital_letter = random.choice("ABCD")
    number = random.randint(1, 9)
    return capital_letter + str(number)
  
  def bag_tag():
    letters = string.ascii_uppercase
    bag_tag = ''.join(random.choices(letters, k=4))
    return bag_tag
  
  print_slowly("Dropping old database tables...")
  session.query(Airline).delete()
  session.query(Flight).delete()
  session.query(Passenger).delete()
  session.query(Bag).delete()
  session.commit()
  print_slowly("Old Airlines, Flights, and Passengers tables deleted")

  print_slowly("Creating new Airline, Flight, and Passenger tables...")
  
  oceanic = Airline(name="Oceanic")
  ajira = Airline(name="Ajira")
  whitestar = Airline(name="White Star")
  colonial = Airline(name="Colonial Fleet")
  uga = Airline(name="United Global Alliance")

  session.add_all([oceanic, ajira, whitestar, colonial, uga])
  session.commit()
  print_slowly("Airlines established")
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
  print_slowly("Flights scheduled")

  flights_list = [o111, o123, a222, a234, w333, w345, c444, c456, u555, u567]
  print_slowly("Flights gathered... compiling passenger lists")

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
  p31 = Passenger(name=fake.name())
  p32 = Passenger(name=fake.name())
  p33 = Passenger(name=fake.name())
  p34 = Passenger(name=fake.name())
  p35 = Passenger(name=fake.name())
  p36 = Passenger(name=fake.name())
  p37 = Passenger(name=fake.name())
  p38 = Passenger(name=fake.name())
  p39 = Passenger(name=fake.name())
  p40 = Passenger(name=fake.name())

  session.add_all([p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p37,p38,p39,p40])
  session.commit()
  print_slowly("Passengers booked")

  b01 = Bag(name=bag_tag(), passenger_id=p01.id)
  b02 = Bag(name=bag_tag(), passenger_id=p02.id)
  b03 = Bag(name=bag_tag(), passenger_id=p03.id)
  b04 = Bag(name=bag_tag(), passenger_id=p04.id)
  b05 = Bag(name=bag_tag(), passenger_id=p05.id)
  b06 = Bag(name=bag_tag(), passenger_id=p06.id)
  b07 = Bag(name=bag_tag(), passenger_id=p07.id)
  b08 = Bag(name=bag_tag(), passenger_id=p08.id)
  b09 = Bag(name=bag_tag(), passenger_id=p09.id)
  b10 = Bag(name=bag_tag(), passenger_id=p10.id)
  b11 = Bag(name=bag_tag(), passenger_id=p11.id)
  b12 = Bag(name=bag_tag(), passenger_id=p12.id)
  b13 = Bag(name=bag_tag(), passenger_id=p13.id)
  b14 = Bag(name=bag_tag(), passenger_id=p14.id)
  b15 = Bag(name=bag_tag(), passenger_id=p15.id)
  b16 = Bag(name=bag_tag(), passenger_id=p16.id)
  b17 = Bag(name=bag_tag(), passenger_id=p17.id)
  b18 = Bag(name=bag_tag(), passenger_id=p18.id)
  b19 = Bag(name=bag_tag(), passenger_id=p19.id)
  b20 = Bag(name=bag_tag(), passenger_id=p20.id)
  b21 = Bag(name=bag_tag(), passenger_id=p21.id)
  b22 = Bag(name=bag_tag(), passenger_id=p22.id)
  b23 = Bag(name=bag_tag(), passenger_id=p23.id)
  b24 = Bag(name=bag_tag(), passenger_id=p24.id)
  b25 = Bag(name=bag_tag(), passenger_id=p25.id)
  b26 = Bag(name=bag_tag(), passenger_id=p26.id)
  b27 = Bag(name=bag_tag(), passenger_id=p27.id)
  b28 = Bag(name=bag_tag(), passenger_id=p28.id)
  b29 = Bag(name=bag_tag(), passenger_id=p29.id)
  b30 = Bag(name=bag_tag(), passenger_id=p30.id)
  b31 = Bag(name=bag_tag(), passenger_id=p31.id)
  b32 = Bag(name=bag_tag(), passenger_id=p32.id)
  b33 = Bag(name=bag_tag(), passenger_id=p33.id)
  b34 = Bag(name=bag_tag(), passenger_id=p34.id)
  b35 = Bag(name=bag_tag(), passenger_id=p35.id)
  b36 = Bag(name=bag_tag(), passenger_id=p36.id)
  b37 = Bag(name=bag_tag(), passenger_id=p37.id)
  b38 = Bag(name=bag_tag(), passenger_id=p38.id)
  b39 = Bag(name=bag_tag(), passenger_id=p39.id)
  b40 = Bag(name=bag_tag(), passenger_id=p40.id)

  session.add_all([b01,b02,b03,b04,b05,b06,b07,b08,b09,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40])
  session.commit()
  print_slowly("Bags are being loaded on the plane... whoops! Dropped one. Got it though. Trust me. It'll ge there at some point...")

  print_slowly("Database Tables Created!  Let's Fly!")
  print_kinda_slow("""
              ______
            _\ _~-\___
    =  = ==(___CLI____D
                \_____\___________________,-~~~~~~~--.._
                /     o o o o o o o o o o o o o o o o  |\_
                `~-.__        ___..----..                  )
                      `---~~\___________/------------``````
                         ===(_________D
  """)
  print_slowly("Enter 'python cli.py' to launch")
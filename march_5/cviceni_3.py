from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import sessionmaker

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

eng = create_engine(f'mysql://root:{password}@localhost:3306/car_rental')

base = declarative_base()


class Cars(base):
    __tablename__ = 'cars'

    car_id = Column(Integer, primary_key=True, autoincrement=True)
    producer = Column(String(30), nullable=False)
    model = Column(String(30), nullable=False)
    year = Column(Integer, nullable=False)
    horse_power = Column(Integer, nullable=False)
    price_per_day = Column(Integer, nullable=False)


class Clients(base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    address = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)


class Bookings(base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, nullable=False)
    car_id = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_amount = Column(Integer, nullable=False)


Session = sessionmaker(bind=eng)
session = Session()

for client in session.query(Clients).all():
    print(client)

for car in session.query(Cars).all():
    print(car)

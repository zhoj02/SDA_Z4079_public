from sqlalchemy import create_engine, text, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.sql import select
from sqlalchemy import join
from sqlalchemy.sql import func
from sqlalchemy import and_

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
    bookings = relationship('Bookings', back_populates='car', cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return f"<Car: id={self.car_id}, producer={self.producer}, model={self.model}, year={self.year}, "
        f"horse_power={self.horse_power}, price_per_day={self.price_per_day}>"


class Clients(base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    address = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)
    bookings = relationship('Bookings', back_populates='client', cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return f"<Client: id={self.client_id}, name={self.name}, surname={self.surname}, address={self.address},"
        f"city={self.city}>"


class Bookings(base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('clients.client_id', ondelete="CASCADE"), nullable=False)
    car_id = Column(Integer, ForeignKey('cars.car_id', ondelete="CASCADE"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_amount = Column(Integer, nullable=False)
    client = relationship('Clients', back_populates='bookings')
    car = relationship('Cars', back_populates='bookings')

    def __repr__(self):
        return f"<Booking: id={self.booking_id}, client_id={self.client_id}, car_id={self.car_id}, "
        f"start_date={self.start_date}, end_date={self.end_date}, total_amount={self.total_amount}>"


Session = sessionmaker(bind=eng)

session = Session()
result = (
    session.query(Clients.client_id, Clients.name, Clients.surname, func.sum(Bookings.total_amount))
    .join(Clients)
    .filter(
        and_(Bookings.end_date <= '2020-07-17', Bookings.start_date >= '2020-07-10')
    )
    .group_by(Clients.client_id)
    .all()
)
print(result)

# Hromadka pro 6:
# 6, 1900
# 6, 1200
#
# Hromadka pro 7:
# 7, 1800
# 7, 1700

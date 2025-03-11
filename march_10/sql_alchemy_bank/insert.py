from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_definition import Transaction, Client, Account
from datetime import datetime

eng = create_engine(f'mysql://root:YourNewPassword@localhost:3306/car_rental')

Session = sessionmaker(bind=eng)

session = Session()

session.add_all(
    [Client(name="jan",surname="novak", address="Praha", birth_date="2024-12-20"),
Client(name="petr",surname="novak", address="Praha", birth_date=datetime(2010,1,1)),
])
session.commit()

print(session.query(Client).all())

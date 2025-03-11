# Cilem je vytvorit 3 tabulky banky
# 1. Tabulka - Clienti - id, jmeno, prijmeni, adresu, datum narozeni
# 2. Ucet - id, cislo_uctu, druh_uctu
# 3. Tabulka - Transakce - id, cislo_uctu_odchozi,  cislo_uctu_prichozi, castka, cas transakce, datum transakce
from datetime import datetime

# Base.metadata.create_all(eng)
# all datatypes imports, not foreign key, only datatypes
from sqlalchemy import Column, String, Integer, DateTime, Time, Date, Any, Float, Boolean

from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import sessionmaker


eng = create_engine(f'mysql+mysqlconnector://root:YourNewPassword@localhost:3306/car_rental')

base = declarative_base()


class Transaction(base):
    # 3. Tabulka - Transakce - id, cislo_uctu_odchozi,  cislo_uctu_prichozi, castka, cas transakce, datum transakce
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    acc_no_out = Column(String(20))
    acc_no_inc = Column(String(20))
    amount = Column(Float)
    date = Column(DateTime, default=datetime.now)


class Client:
    # 1. Tabulka - Clienti - id, jmeno, prijmeni, adresu, datum narozeni

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    surname = Column(String(20))
    address = Column(String(20))
    birth_date = Column(Date)


class Accounts:
    # 2. Ucet - id, cislo_uctu, druh_uctu

    id = Column(Integer, primary_key=True, autoincrement=True)
    cislo_uctu = Column(String(20))
    druh_uctu = Column(String(20))


base.metadata.drop_all(eng)
base.metadata.create_all(eng)

Session = sessionmaker(bind=eng)
session = Session()
print(session.query(Transaction).all())

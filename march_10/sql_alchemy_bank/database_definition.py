# Cilem je vytvorit 3 tabulky banky
# 1. Tabulka - Clienti - id, jmeno, prijmeni, adresu, datum narozeni
# 2. Ucet - id, cislo_uctu, druh_uctu
# 3. Tabulka - Transakce - id, cislo_uctu_odchozi,  cislo_uctu_prichozi, castka, cas transakce, datum transakce
from datetime import datetime

# Base.metadata.create_all(eng)
# all datatypes imports, not foreign key, only datatypes
from sqlalchemy import Column, String, Integer, DateTime, Time, Date, Any, Float, Boolean

from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker

base = declarative_base()


class Account(base):
    # 2. Ucet - id, cislo_uctu, druh_uctu
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey(column='client.id', ondelete="CASCADE"))
    cislo_uctu = Column(String(20))
    druh_uctu = Column(String(20))
    client = relationship('Clients')


class Client(base):
    # 1. Tabulka - Clienti - id, jmeno, prijmeni, adresu, datum narozeni
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    surname = Column(String(20))
    address = Column(String(20))
    birth_date = Column(Date)
    accounts = relationship('Account')


class Transaction(base):
    # 3. Tabulka - Transakce - id, cislo_uctu_odchozi,  cislo_uctu_prichozi, castka, cas transakce, datum transakce
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    acc_no_out = Column(Integer, ForeignKey(column='account.id'))
    acc_no_inc = Column(Integer, ForeignKey(column='account.id', ondelete='cascade'))
    amount = Column(Float)
    date = Column(DateTime, default=datetime.now)

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from database_definition import Transaction, Client, Account
from datetime import datetime

eng = create_engine(f'mysql+mysqlconnector://root:YourNewPassword@localhost:3306/car_rental')

Session = sessionmaker(bind=eng)

session = Session()

# session.add_all(
#     [Client(name="jan",surname="novak", address="Praha", birth_date="2024-12-20"),
# Client(name="petr",surname="novak", address="Praha", birth_date=datetime(2010,1,1)),
# ])
# session.commit()
#
# session.add_all(
#     [Account(client_id=1, cislo_uctu="1478478547", druh_uctu="sporici"),
#     Account(client_id=1, cislo_uctu="178547414", druh_uctu="bezny"),
#      ]
# )
session.commit()
result = session.query(Client).all()
for i in result:
    for account in i.accounts:
        print(account.cislo_uctu)


# print(session.execute(text("SELECT * FROM client")).all())


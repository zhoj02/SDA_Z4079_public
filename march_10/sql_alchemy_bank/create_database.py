from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

eng = create_engine(f'mysql+mysqlconnector://root:YourNewPassword@localhost/')

Session = sessionmaker(bind=eng)
session = Session()

result = session.execute(text("SELECT 1")).all()
print(result)
# Vytvorit databazi s nazvem bank
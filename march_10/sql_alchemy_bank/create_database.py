from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

eng = create_engine(f'mysql://root:YourNewPassword@localhost:3306/')

Session = sessionmaker(bind=eng)
session = Session()

result = session.execute(text())
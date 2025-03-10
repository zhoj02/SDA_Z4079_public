# insert 3 klienty
# [('client_id', 'int', 'NO', 'PRI', None, 'auto_increment'),
# ('name', 'varchar(30)', 'NO', '', None, ''),
# ('surname', 'varchar(30)', 'NO', '', None, ''),
# ('address', 'varchar(30)', 'NO', '', None, ''),
# ('city', 'varchar(30)', 'NO', '', None, '')]
from mysql.connector import connect

with connect(user="root", password="YourNewPassword", database="car_rental") as conn:
    with conn.cursor() as cursor:
        cursor.execute("DESCRIBE clients")
        print(cursor.fetchall())

with connect(user="root", password="YourNewPassword", database="car_rental") as conn:
    with conn.cursor() as cursor:
        cursor.execute("""
        INSERT INTO clients (name, surname, address, city)
        VALUES 
        ('jan', 'pavel', 'Sokolovská','Prague'),
        ('maria', 'majerova', 'Sokolovská','Brno'),
        ('jan', 'honzik', 'Sokolovská','Ostrava')
        """)
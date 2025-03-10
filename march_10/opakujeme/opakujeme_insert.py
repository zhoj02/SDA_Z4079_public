# insert 3 klienty

from mysql.connector import connect

with connect(user="root", password="YourNewPassword", database="car_rental") as conn:
    with conn.cursor() as cursor:
        ...
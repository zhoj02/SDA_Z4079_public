# Vyber bookings, ktere maji vyssi hodnotu nez 500

from mysql.connector import connect

with connect(user="root", password="YourNewPassword", database="car_rental") as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM bookings WHERE total_amount > 500")
        print(cursor.fetchall())

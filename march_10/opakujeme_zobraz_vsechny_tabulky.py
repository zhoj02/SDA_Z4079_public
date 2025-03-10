# Dejte print vsech tabulek v databazi car_rental
# Databazi definujte v connect funkci
# prikaz na to je: SHOW TABLES

from mysql.connector import connect

with connect(user="root", password="YourNewPassword", database="car_rental") as conn:
    with conn.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        print(cursor.fetchall())

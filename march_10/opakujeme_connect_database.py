from mysql.connector import connect

with connect(user="root", password="YourNewPassword") as conn:
    with conn.cursor() as cursor:
        cursor.execute("SHOW DATABASES")
        print(cursor.fetchall())

from mysql.connector import connect

conn = connect(host="localhost", user="root", password="YourNewPassword")
test_select = "SELECT 1;"

cursor = conn.cursor()

cursor.execute(test_select)
print(cursor.fetchall())
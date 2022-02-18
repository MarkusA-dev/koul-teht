import pyodbc
import time
cnxn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=localhost;DATABASE=ORDERBASE;Trusted_Connection=yes')
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM ordertable")
row = cursor.fetchone()
while row:
    print(f"{row[1]} || {row[2]} || {row[3]}")
    row  = cursor.fetchone()
time.sleep(1)

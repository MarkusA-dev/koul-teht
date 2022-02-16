import pyodbc
import time

server = 'localhost'
database = 'testdb'

cnxn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER='
                      +server+';DATABASE='+database+';Trusted_Connection=yes')
cursor = cnxn.cursor()
rows = cursor.execute("SELECT * FROM TestTable").fetchall()
cursor.execute("SELECT * FROM TestTable")
row = cursor.fetchone()
while row:
    print(f"{row[1]} || {row[2]} || {row[3]}")
    row  = cursor.fetchone()
time.sleep(10)

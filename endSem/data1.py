import mysql.connector
cn=mysql.connector.connect(
    host = "localhost",
    user="root",
    password=""
)
if cn:
    print("connected")
else:
    print("not connected")
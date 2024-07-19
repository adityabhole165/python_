import mysql.connector 

cn=mysql.connector.connect (
    host="localhost",  # your MySQL server's host name or IP address
    user="root"
)

if cn:
    print("Connected to database")
else:
    print("Failed to connect to database ")
cn.close()
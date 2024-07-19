import mysql.connector
cn = mysql.connector.connect(
    database="python",
    host="localhost",
    user="root",
)
if cn:
    print("Connected to database")
    cur=cn.cursor()
    cur.execute("select * from course")
    for row in cur:
        print(row)

    cur.close()
else:
    print("Failed to connect to database ")
cn.close()
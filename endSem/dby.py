import mysql.connector
cn = mysql.connector.connect(
    database="python",
    host="localhost",
    user="root",
    # charset="utf8mb4",
    # collection="utf8mb4_unicode_ci"
)
if cn:
    print("connection successful")
    # databases=()
    # show databases
    # cr.execute("show databases")
    # for db in cr:
        # print(db)
    
    # show table using cursor
    # cr.execute("select* from course")
    # for r in cr:
    #     print(r)
        # print("course_name", r[1],"Fees ",r[3])

    
    # show table using record set 
    # cr.execute("select* from course")
    # cr.execute("select course_name ,fees from course")
    # res=cr.fetchall()
    # for r in res:
        # for all records
        # print(r)

        # course name
        # print(r[1])
        # print(r)
        
        
    # program to display selected records only
    v=input("enter course number =")
    cr=cn.cursor()
    
    
    cr.execute("select * FROM c  " + v)
    res=cr.fetchall()
    print("course name = ",res[1])
    print("course durattion =",res[2])
    print("course fees =",res[3])
    
    cr.close()
else:
    print("Failed to connect to database ")
cn.close()
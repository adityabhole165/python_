import mysql.connector
# import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            # passwd=user_password,
            database="python"
        )
        print("Connection to database successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("localhost", "root", "", "student_record")
if connection.is_connected():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student")
    student_records = cursor.fetchall()
    for row in student_records:
        print(row)

    cursor.execute("SELECT * FROM course")
    course_records = cursor.fetchall()
    for row in course_records:
        print(row)

    roll_no = input("Enter roll no: ")
    cursor.execute("SELECT SUM(rec_amt) FROM student_fees WHERE rno = %s", (roll_no,))
    result = cursor.fetchone()
    if result:
        print(f"Total paid fees for roll no {roll_no} is: {result[0]}")

    cursor.close()
    connection.close()
    print("Connection closed")

    
    
    
    
    
    
    
    
    
    
    
    
    
    # vrno=(input("enter roll no ="))
    # curr=cn.cursor()
    # curr.execute("select * from student")
    # for row in curr:
    #     print(row)
    # curr.execute("select * from course")
    # for row in curr:
    #     print(row)
    # res1=curr.execute("select sum(rec_amt) from student_fees where rno= ")
    # print(res1)
    # vsname=res1[0]
    # res2=curr.execute("select fees from course where cno=(select cno from student where rno=)"+vrno)
    # print(res1)
    
    # vcfees=res2[0]
    # vrfees=vcfees
    # print(f"rno={vrno} and fees ={vrfees}")
# else:
#     print("Failed to connect to MySQL")
# cn.close()
    
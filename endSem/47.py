def cal(**kvlp):
    print("parameters and its values are :")
    for key,value in kvlp.items():
        print(f"key={key} and values={value}")
        print("end of the function")

# cal(n1=9)
cal(name="Aditya",CGPA=9.8)
# cal(num1=8,num2=6,num3=14)
# print("end")
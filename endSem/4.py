n1=int(input("enter first number ="))
n2=int(input("entyer second number= "))
n3=int(input("entyer third number= "))

if(n1>n2):
    if(n1>n3):
        print("max number is" , n1)
    else:
        print("max number is ",n3)
else:
    if(n2>n3):
        print("max number is ",n2);
    else:
        print("max is ",n3)

print("end......")
    
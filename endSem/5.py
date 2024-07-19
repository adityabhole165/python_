n1=int(input("enter the first number ="))
n2=int(input("enter the second number ="))
n3=int(input("enter the third number ="))

if(n1>n2):
    max=n3
    if(n1>n3):
        max=n1
else:
    max=n3
    if(n2>n3):
        max=n2
        
print("maximum number is =",max)
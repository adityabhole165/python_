n1=int(input("enetr first number ="))
n2=int(input("enter second number ="))
n3=int(input("enter third number = "))
if(n1>n2):
    max=n1
else:
    max=n2
if(n3>max):
    max=n3
print("largest number is",max)

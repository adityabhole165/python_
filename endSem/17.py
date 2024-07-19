n=int(input("enter any number "))
se=0
so=0
ce=0
co=0
while(True):
    b=n%10
    n//=10
    if(b%2==0):
        se+=b
        ce+=1
    else:
        so+=b
        co+=1
    if(n==0):
        break
avge=se/ce
avgeo=so/co
print(f"average of even {avge},average of odd {avgeo}")
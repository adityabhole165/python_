n=int(input("enter any number "))
sum=0
while(True):
    b=n%10
    n=n//10
    sum+=b;
    if(n==0):
        break;
print("addition of digits ",sum);
n=int(input("enter any number "));
sum=0
count=0
rev=0
while(True):
    b=n%10
    n//=10
    rev=rev*10+b
    if(n==0):
        break;
while(True):
    c=rev%10
    rev//=10
    sum+=c
    count+=1
    if(rev==0)and(count==2):
        break

print("addition of first and last digit is ",sum)
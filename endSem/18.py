sum=0
n=int(input("enter any number "))
if(n<10):
    sum+=n
if(n<100):
    sum+=n%10 + n//10
else:
    sum=n%10
    while(True):
        n//=10
        if(n<10):
            break
    sum+=n
print("sum of first and last digit is ", sum)
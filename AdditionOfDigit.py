n=int(input("input any nos"))
sum=0
while(True):
    b=n%10
    n=n//10
    sum+=b
    if(n==0):
        break
print("\n additipn of digits",(sum))

    
    
    

print("enter 10 numbers :")
sum=0;
for r in range(10):
    num=int(input())
    if(r>6):
        sum+=num
        
print("average of last 3 numbers =",sum/3)
    
print("enter 10 numbers:" )
sum=0
count=0
avg=0
for a in range(10):
    num=int(input())
    if(num%2==0) and (count<2):
        sum+=num
        count+=1
if(count==0):
    avg=0
elif(count==1):
    avg=sum
else:
    avg=sum/count
print("average of even numbers only :",avg)
# binary search desending order
print("enter any 10 elements")
li=[]
for r in range(10):
    li.append(int(input()))
n=int(input("enter number to search"))
li.sort(reverse=True)
low,high=0,9
while low<=high:
    mid=(low+high)//2
    if li[mid]==n:
        print(f"%d is present " %(n))
        break
    elif li[mid]<n:
        high=mid-1 
    else:
        low=mid+1
        
else:
    print("%d is not present " %(n))
print("end of searching")
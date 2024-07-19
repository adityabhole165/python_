# binary search
# binary search required list in pre ordered format
print("enter any 10 elements")
li=[]
for r in range(10):
    li.append(int(input()))
n=int(input("enter number to search"))
li.sort()
low,high=0,9
while low<=high:
    mid=(low+high)//2
    if li[mid]==n:
        print(f"%d is present " %(n))
        break
    elif li[mid]<n:
        low=mid+1
    else:
        high=mid-1 
else:
    print("%d is not present " %(n))
print("end of searching")